import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "This is normal text", None, {"href": "https://www.google.com"})
        self.assertEqual(
            " href= https://www.google.com",
            node.props_to_html()
        )
    
    def test_few_props(self):
        node = HTMLNode("p", "This is normal text", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(
            " href= https://www.google.com target= _blank",
            node.props_to_html()
        )
    
    def test_repr(self):
        node = HTMLNode("div", "Text as usual", None, {'href': 'https://www.google.com'})
        self.assertEqual(
            "HTMLNode(div, Text as usual, children: None, {'href': 'https://www.google.com'})",
            node.__repr__()
        )
