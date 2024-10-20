import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "div",
            "Hello world!",
            props={"href": "https://www.google.com", "target": "_blank"},
        )
        self.assertEqual(
            node.props_to_html(), 
            ' href="https://www.google.com" target="_blank"',
            )
    
    def test_values(self):
        node = HTMLNode(
            "div",
            "Backend is great so far.",
            None,
            {"href": "https://.boot.dev"}
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "Backend is great so far.",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            {"href": "https://.boot.dev"},
        )
    
    def test_repr(self):
        node = HTMLNode(
            "div",
            "Well hello there!",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(tag: div, value: Well hello there!, children: None, props: {'class': 'primary'})"
        )
    
    def test_leaf_to_html(self):
        node = LeafNode(
            "p",
            "Let that sink in",
        )
        self.assertEqual(
            node.to_html(),
            "<p>Let that sink in</p>",
            )
    
    def test_leaf_url(self):
        node = LeafNode(
            "a",
            "Click me!",
            {"href": "https://www.google.com"},
        )
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>'
        )

    def test_leaf_fail(self):
        node = LeafNode(
            "a",
            None,
        )
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
