import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_url(self):
        node = TextNode("Text node with a url", TextType.ITALIC, "www.google.com")
        node2 = TextNode("Text node with a url", TextType.ITALIC, "www.google.com")
        self.assertEqual(node, node2)
    
    def test_none_url(self):
        node = TextNode("None Url", TextType.LINK, None)
        node2 = TextNode("None Url", TextType.LINK)
        self.assertEqual(node, node2)

    def test_obj(self):
        node = TextNode(1, TextType.IMAGE)
        node2 = TextNode(1, TextType.IMAGE)
        self.assertEqual(node, node2)
    
    def test_eq_false(self):
        node = TextNode("Note equal", TextType.IMAGE)
        node2 = TextNode("Note equal", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_value(self):
        node = TextNode("Node 1 is not equal to node 2", TextType.BOLD)
        node2 = TextNode("Node 2 is not equal to node 1", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

if __name__ == "__main__":
    unittest.main()