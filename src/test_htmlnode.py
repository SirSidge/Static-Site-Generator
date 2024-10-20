import unittest
from htmlnode import HTMLNode

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


if __name__ == "__main__":
    unittest.main()
