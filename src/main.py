from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode


def text_node_to_html_node(text_node: TextNode) -> LeafNode:

    

    html_node = LeafNode('', '')
    return html_node

def main():
    some_node = TextNode(text='This is some anchor text', text_type=TextType.LINK, url='https://www.boot.dev')
    print(some_node)


if __name__ == '__main__':
    main()
