from src.textnode import TextType, TextNode
from src.htmlnode import HTMLNode, LeafNode, ParentNode
from src.functions import *


def main():
    some_node = TextNode(text='This is some anchor text', text_type=TextType.LINK, url='https://www.boot.dev')
    print(some_node)


if __name__ == '__main__':
    main()
