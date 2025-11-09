import unittest

from src.textnode import TextNode, TextType
from src.functions import text_to_textnodes


class TestToTextnodes(unittest.TestCase):
    def test_full(self):
        text_md: str = 'This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
        text_nodes: list[TextNode] = text_to_textnodes(text_md)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            text_nodes
        )
    def test_bold(self):
        text: str = '**bold text**'
        new_node: list[TextNode] = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode('bold text', TextType.BOLD)
            ],
            new_node
        )

    def test_italic(self):
        text: str = '_italic text_'
        new_node: list[TextNode] = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode('italic text', TextType.ITALIC)
            ],
            new_node
        )

    def test_code(self):
        text: str = '`code text`'
        new_node: list[TextNode] = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode('code text', TextType.CODE)
            ],
            new_node
        )

    def test_image(self):
        text: str = '![image](images/image)'
        new_node: list[TextNode] = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode('image', TextType.IMAGE, 'images/image')
            ],
            new_node
        )

    def test_link(self):
        text: str = '[link](links/link)'
        new_node: list[TextNode] = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode('link', TextType.LINK, 'links/link')
            ],
            new_node
        )
