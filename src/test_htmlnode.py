import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_parentNode(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_no_children(self):
        node = ParentNode(
            "div",
            None,
        )
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_nested_parents(self):
        node = ParentNode(
            "div",
            [
                LeafNode("b", "YOU SHALL NOT PASS!"),
                ParentNode("i", [
                    LeafNode("i", "unless I say so"),
                ]),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            '<div><b>YOU SHALL NOT PASS!</b><i><i>unless I say so</i></i>Normal text</div>',
        )

    def test_parent_props(self):
        node = ParentNode(
            "div",
            [
                LeafNode("b", "Here we go again..."),
            ],
            {"href": "https://www.google.com"}
        )
        self.assertEqual(
            node.to_html(),
            '<div href="https://www.google.com"><b>Here we go again...</b></div>'
        )

if __name__ == "__main__":
    unittest.main()
