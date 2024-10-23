import unittest
from markdownnode import split_nodes_delimiter
from textnode import TextNode, TextType

class TestMarkdownNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        node2 = TextNode("This text should contain a **bold** word", TextType.TEXT)
        node3 = TextNode("Here we'll test how well *italics* works", TextType.TEXT)
        node4 = TextNode("Here we'll test how well `code block` works", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, node4], "`", TextType.CODE)
        new_nodes2 = split_nodes_delimiter([node2], "**", TextType.BOLD)
        new_nodes3 = split_nodes_delimiter([node3], "*", TextType.ITALIC)
        self.assertEqual(
            f"{new_nodes}",
            "[TextNode(This is text with a , TextType.TEXT, None), TextNode(code block, TextType.CODE, None), TextNode( word, TextType.TEXT, None), TextNode(Here we'll test how well , TextType.TEXT, None), TextNode(code block, TextType.CODE, None), TextNode( works, TextType.TEXT, None)]"
        )
        self.assertEqual(
            f"{new_nodes2}",
            '[TextNode(This text should contain a , TextType.TEXT, None), TextNode(bold, TextType.BOLD, None), TextNode( word, TextType.TEXT, None)]'
        )
        self.assertEqual(
            f"{new_nodes3}",
            "[TextNode(Here we'll test how well , TextType.TEXT, None), TextNode(italics, TextType.ITALIC, None), TextNode( works, TextType.TEXT, None)]"
        )

if __name__ == "__main__":
    unittest.main()