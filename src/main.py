from textnode import TextNode, TextType

def main():
    text_node = TextNode("This is the text", TextType.BOLD, "www.boot.dev")
    print(text_node.__repr__())

main()