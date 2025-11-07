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


def main():
    some_node = TextNode(text='This is some anchor text', text_type=TextType.LINK, url='https://www.boot.dev')
    print(some_node)


if __name__ == '__main__':
    main()
