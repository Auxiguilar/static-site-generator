import unittest

from src.htmlnode import HTMLNode, LeafNode, ParentNode


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

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html(self):
        node1 = LeafNode("p", "Hello, world!")
        self.assertEqual(node1.to_html(), "<p>Hello, world!</p>")
        node2props = {"href": "https://www.google.com"}
        node2 = LeafNode(tag='a', value='This is a link!', props=node2props)
        self.assertEqual(node2.to_html(), '<a href="https://www.google.com">This is a link!</a>')


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
            )
    def test_to_html_multiple_children(self):
        child1 = LeafNode(tag='p', value='Top text.')
        child2 = LeafNode(tag='p', value='Middle text.')
        child3 = LeafNode(tag='p', value='Bottom text.')
        parent = ParentNode(tag='div', children=[child1, child2, child3])
        self.assertEqual(
            parent.to_html(),
            '<div><p>Top text.</p><p>Middle text.</p><p>Bottom text.</p></div>'
            )
