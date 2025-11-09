import re

from src.textnode import TextType, TextNode, BlockType
from src.htmlnode import HTMLNode, LeafNode, ParentNode


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag='b', value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag='i', value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag='code', value=text_node.text)
        case TextType.LINK:
            return LeafNode(tag='a', value=text_node.text, props={'href': str(text_node.url)})
        case TextType.IMAGE:
            return LeafNode(tag='img', value='', props={'src': str(text_node.url), 'alt': text_node.text})
        case _:
            raise LookupError(f'TextNode has no or improper TextType: {text_node.text_type}')

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    valid_delimiters: list[str] = ['**', '_', '`']
    if delimiter not in valid_delimiters:
        raise ValueError(f'Delimiter must be: {valid_delimiters}.')
    new_nodes: list[TextNode] = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        delimiter_count: int = 0
        for char in node.text:
            if char == delimiter[0:1]:
                delimiter_count += 1
        if delimiter_count % 2 != 0:
            raise SyntaxError(f'Invalid Markdown syntax: "{node.text}"')
        
        nodes: list[TextNode] = []
        parts: list[str] = node.text.split(sep=delimiter)
        for part in parts:
            if not part: # woops!
                continue
            if (part.startswith(' ')
                or part.endswith(' ')
                or valid_delimiters[0] in part
                or valid_delimiters[1] in part
                or valid_delimiters[2] in part):
                nodes.append(TextNode(text=part, text_type=TextType.TEXT))
            else:
                nodes.append(TextNode(text=part, text_type=text_type))
        new_nodes.extend(nodes)
    return new_nodes

def extract_markdown_images(text: str) -> list[tuple]:
    images: list[tuple] = re.findall(r'!\[([^\[\]]*)\]\(([^\(\)]*)\)', text)
    return images

def extract_markdown_links(text: str) -> list[tuple]:
    links: list[tuple] = re.findall(r'(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)', text)
    return links

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        images: list[tuple] = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue
        text: str = node.text
        for img in images:
            alt: str = img[0]
            url: str = img[1]
            parts: list[str] = text.split(sep=f'![{alt}]({url})')
            if not parts[0]:
                new_nodes.append(TextNode(text=alt, text_type=TextType.IMAGE, url=url))
                text: str = parts[1]
            else:
                new_nodes.append(TextNode(text=parts[0], text_type=TextType.TEXT))
                new_nodes.append(TextNode(text=alt, text_type=TextType.IMAGE, url=url))
                text: str = parts[1]
        if text:
            new_nodes.append(TextNode(text=text, text_type=TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        links: list[tuple] = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
            continue
        text: str = node.text
        for link in links:
            anchor: str = link[0]
            url: str = link[1]
            parts: list[str] = text.split(sep=f'[{anchor}]({url})')
            if not parts[0]:
                new_nodes.append(TextNode(text=anchor, text_type=TextType.LINK, url=url))
                text: str = parts[1]
            else:
                new_nodes.append(TextNode(text=parts[0], text_type=TextType.TEXT))
                new_nodes.append(TextNode(text=anchor, text_type=TextType.LINK, url=url))
                text: str = parts[1]
        if text:
            new_nodes.append(TextNode(text=text, text_type=TextType.TEXT))
    return new_nodes

def text_to_textnodes(text: str) -> list[TextNode]:
    find_images: list[TextNode] = split_nodes_image([TextNode(text, TextType.TEXT)])
    find_links: list[TextNode] = split_nodes_link(find_images)
    format_bold: list[TextNode] = split_nodes_delimiter(find_links, '**', TextType.BOLD)
    format_italics: list[TextNode] = split_nodes_delimiter(format_bold, '_', TextType.ITALIC)
    format_code: list[TextNode] = split_nodes_delimiter(format_italics, '`', TextType.CODE)
    return format_code

def markdown_to_blocks(markdown: str) -> list[str]:
    blocks: list[str] = []
    parts: list[str] = markdown.split('\n\n')
    for part in parts:
        if not part or part == '\n':
            continue
        blocks.append(part.strip())
    return blocks

def block_to_blocktype(block: str) -> BlockType:
    if block.startswith('#') and '# ' in block: # who cares how many there are?
        return BlockType.HEADING
    elif block.startswith('```') and block.endswith('```'):
        return BlockType.CODE
    parts: list[str] = block.split('\n')
    quote_count: int = 0
    for part in parts:
        if part.startswith('>'):
            quote_count += 1
    if len(parts) == quote_count:
        return BlockType.QUOTE
    ulist_count: int = 0
    for part in parts:
        if part.startswith('- '):
            ulist_count += 1
    if len(parts) == ulist_count:
        return BlockType.UNORDERED_LIST
    olist_count: int = 1
    for part in parts:
        if part.startswith(f'{olist_count}. '):
            olist_count += 1
    if len(parts) == olist_count - 1:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH


# BUILD EVERYTHING!
# or: make a div
def markdown_to_html_node(markdown: str) -> ParentNode:
    text_blocks: list[str] = markdown_to_blocks(markdown=markdown)
    children: list[LeafNode] = []

    for block in text_blocks:
        tag: str = match_block_type(block_to_blocktype(block=block))
        text_nodes: list[TextNode] = text_to_textnodes(block)

    parent_node: ParentNode = ParentNode(tag='div', children=[])
    return parent_node

def match_block_type(block_type: BlockType) -> str:
    match block_type:
        case BlockType.PARAGRAPH:
            return 'p'
        case BlockType.CODE:
            return 'pre'
        case BlockType.HEADING:
            return 'h' # we have a problem
        case BlockType.QUOTE:
            return 'blockquote'
        case BlockType.UNORDERED_LIST:
            return 'ul'
        case BlockType.ORDERED_LIST:
            return 'ol'
        case _:
            raise ValueError(f'{block_type} is not a BlockType')
