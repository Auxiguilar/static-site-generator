import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.ITALIC)
        node4 = TextNode("This is a text node", TextType.ITALIC)
        node5 = TextNode("This is an image", TextType.BOLD)
        node6 = TextNode("This is an image", TextType.BOLD)
        node7 = TextNode("This is an image", TextType.BOLD, None)
        self.assertEqual(node, node2)
        self.assertEqual(node3, node4)
        self.assertEqual(node5, node6)
        self.assertEqual(node6, node7)

    def test_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        node3 = TextNode("This is an text node", TextType.ITALIC)
        node4 = TextNode("This is a link node", TextType.LINK, None)
        node5 = TextNode("This is a link node", TextType.LINK, "peekaboo")
        node6 = TextNode("This is a link node", TextType.LINK)
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node2, node3)
        self.assertNotEqual(node4, node5)
        self.assertNotEqual(node5, node6)


if __name__ == "__main__":
    unittest.main()