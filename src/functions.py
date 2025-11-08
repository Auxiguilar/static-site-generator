from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode


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
