import unittest

from src.functions import split_nodes_image, split_nodes_link
from src.textnode import TextNode, TextType


class TestSplitLinkImage(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            'This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)',
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode('This is text with an ', TextType.TEXT),
                TextNode('image', TextType.IMAGE, 'https://i.imgur.com/zjjcJKZ.png'),
                TextNode(' and another ', TextType.TEXT),
                TextNode(
                'second image', TextType.IMAGE, 'https://i.imgur.com/3elNhQu.png'
                ),
            ],
            new_nodes,
        )
        self.assertEqual(4, len(new_nodes))

    def test_split_links(self):
        node = TextNode(
            'This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)',
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(4, len(new_nodes))
        self.assertListEqual(
            [
                TextNode('This is text with a link ', TextType.TEXT),
                TextNode('to boot dev', TextType.LINK, 'https://www.boot.dev'),
                TextNode(' and ', TextType.TEXT),
                TextNode(
                'to youtube', TextType.LINK, 'https://www.youtube.com/@bootdotdev'
                ),
            ],
            new_nodes,
        )
