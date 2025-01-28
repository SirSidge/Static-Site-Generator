import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "This is normal text", None, {"href": "https://www.google.com"})
        self.assertEqual(
            " href=https://www.google.com",
            node.props_to_html()
        )
    
    def test_few_props(self):
        node = HTMLNode("p", "This is normal text", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(
            " href=https://www.google.com target=_blank",
            node.props_to_html()
        )
    
    def test_repr(self):
        node = HTMLNode("div", "Text as usual", None, {'href': 'https://www.google.com'})
        self.assertEqual(
            "HTMLNode(div, Text as usual, children: None, {'href': 'https://www.google.com'})",
            node.__repr__()
        )

    def test_leaf(self):
        node = LeafNode("p", "I hope Boot.dev is the answer.", {'href': 'https://www.boot.dev'})
        self.assertEqual(
            "<p href=https://www.boot.dev>I hope Boot.dev is the answer.</p>",
            node.to_html()
        )
        #Just text
        node2 = LeafNode("", "Text without tag", {})
        self.assertEqual(
            "Text without tag",
            node2.to_html()
        )
        #Value error if no text given
        node3 = LeafNode("p", "", {'href': 'https://www.boot.dev'})
        with self.assertRaises(ValueError):
            node3.to_html()
    
    def test_leaf_repr(self):
        node = LeafNode("p", "I hope Boot.dev is the answer.", {'href': 'https://www.boot.dev'})
        self.assertEqual(
            "LeafNode(p, I hope Boot.dev is the answer., {'href': 'https://www.boot.dev'})",
            node.__repr__()
        )