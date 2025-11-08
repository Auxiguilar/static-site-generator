import unittest

from textnode import TextNode, TextType
from functions import split_nodes_delimiter


class TestSplitNodes(unittest.TestCase):
    def test_invalid_md(self):
        wrong_node: list[TextNode] = [
            TextNode(text='This is **not* proper bold.', text_type=TextType.TEXT)
            ]
        with self.assertRaises(SyntaxError):
            fail = split_nodes_delimiter(old_nodes=wrong_node, delimiter='**', text_type=TextType.BOLD)

    def test_invalid_delimiter(self):
        node: list[TextNode] = [
            TextNode(text='This is normal text.', text_type=TextType.TEXT)
        ]
        with self.assertRaises(ValueError):
            invalid_delimiter = split_nodes_delimiter(old_nodes=node, delimiter='', text_type=TextType.TEXT)
        with self.assertRaises(ValueError):
            invalid_delimiter = split_nodes_delimiter(old_nodes=node, delimiter=' ', text_type=TextType.TEXT)
        with self.assertRaises(ValueError):
            invalid_delimiter = split_nodes_delimiter(old_nodes=node, delimiter='*', text_type=TextType.TEXT)
    
    def test_correct_node(self):
        correct_node: list[TextNode] = [
            TextNode(text='This **is** proper bold.', text_type=TextType.TEXT)
        ]
        result: list[TextNode] = split_nodes_delimiter(old_nodes=correct_node, delimiter='**', text_type=TextType.BOLD)
        self.assertEqual(3, len(result))
        self.assertEqual(TextType.BOLD, result[1].text_type)
        self.assertNotEqual(TextType.BOLD, result[0].text_type)
    
    def test_multiple_nodes(self):
        nodes: list[TextNode] = [
            TextNode(text='This **is** proper bold.', text_type=TextType.TEXT),
            TextNode(text='This is _proper_ italics!', text_type=TextType.TEXT)
        ]
        result: list[TextNode] = split_nodes_delimiter(old_nodes=nodes, delimiter='_', text_type=TextType.ITALIC)
        self.assertEqual(TextType.ITALIC, result[2].text_type)
        self.assertEqual(' italics!', result[3].text)

    def test_skip_already_formatted(self):
        nodes: list[TextNode] = [
            TextNode(text='This **is** proper bold.', text_type=TextType.TEXT),
            TextNode(text='This is proper italics!', text_type=TextType.ITALIC)
        ]
        result: list[TextNode] = split_nodes_delimiter(old_nodes=nodes, delimiter='**', text_type=TextType.BOLD)
        self.assertEqual(result[-1].text, 'This is proper italics!')
        self.assertEqual(4, len(result))

    def test_completed_formatting(self):
        nodes: list[TextNode] = [
            TextNode(text='This **is** proper bold.', text_type=TextType.TEXT),
            TextNode(text='This is _proper_ italics!', text_type=TextType.TEXT),
            TextNode(text='This is a `code` block...', text_type=TextType.TEXT)
        ]
        bolded: list[TextNode] = split_nodes_delimiter(old_nodes=nodes, delimiter='**', text_type=TextType.BOLD)

        # part.text for part in bolded:
        # ['This ', 'is', ' proper bold.', 'This is _proper_ italics!']
        # length of 4
        self.assertEqual('is', bolded[1].text)
        self.assertEqual('This is _proper_ italics!', bolded[3].text)
        self.assertEqual(bolded[3].text_type, TextType.TEXT)
        self.assertEqual(5, len(bolded))

        italics: list[TextNode] = split_nodes_delimiter(old_nodes=bolded, delimiter='_', text_type=TextType.ITALIC)
        self.assertEqual(italics[0].text, 'This ')
        self.assertEqual(italics[1].text, 'is')
        self.assertEqual(italics[2].text, ' proper bold.')
        self.assertEqual(italics[3].text, 'This is ')
        self.assertEqual(italics[4].text, 'proper')
        self.assertEqual(italics[5].text, ' italics!')

        coded: list[TextNode] = split_nodes_delimiter(old_nodes=italics, delimiter='`', text_type=TextType.CODE)
        self.assertEqual(coded[7].text_type, TextType.CODE)

