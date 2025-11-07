import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node1 = HTMLNode()
        self.assertEqual(node1.props_to_html(), '')
        node2props = {
            "href": "https://www.google.com",
            "target": "_blank"
            }

        node2 = HTMLNode(props=node2props)
        self.assertEqual(node2.props_to_html(), ' href="https://www.google.com" target="_blank"')
        self.assertNotEqual(node1.props_to_html(), node2.props_to_html())
        self.assertEqual(f'{node1}', 'HTMLNode(None, None, None, None)')
        node3 = HTMLNode(props={})
        self.assertEqual(node1.props_to_html(), node3.props_to_html())
