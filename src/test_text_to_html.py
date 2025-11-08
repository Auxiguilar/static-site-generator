import unittest

from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextType, TextNode
from functions import text_node_to_html_node


class TestTextToHTML(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode('This is a bold node', TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, 'This is a bold node')

    def test_italic(self):
        node = TextNode('This is an italic node', TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'i')
        self.assertEqual(html_node.value, 'This is an italic node')

    def test_code(self):
        node = TextNode('This is a code node', TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'code')
        self.assertEqual(html_node.value, 'This is a code node')
    
    def test_link(self):
        node = TextNode('This is a link node', TextType.LINK)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.value, 'This is a link node')
        assert html_node.props is not None
        self.assertEqual(html_node.props['href'], 'None')
    
    def test_image(self):
        node = TextNode(text='This is an image node', text_type=TextType.IMAGE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'img')
        assert html_node.props is not None
        self.assertEqual(html_node.props['alt'], 'This is an image node')
    
    def test_no_type(self):
        node = TextNode('This is a text node', None) # type: ignore
        with self.assertRaisesRegex(LookupError, 'TextNode has no or improper TextType: None') as le:
            html_node = text_node_to_html_node(node)
