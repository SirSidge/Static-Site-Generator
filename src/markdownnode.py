from textnode import TextNode, TextType, text_node_to_html_node

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_code = []
    for node in old_nodes:
        new_node = node.text.split(delimiter)
        if len(new_node) % 2 == 0:
            raise Exception("Invalid Markdown, formatting section not closed")
        counter = 0
        for element in new_node:
            if counter % 2 == 0:
                new_code.extend([TextNode(element, TextType.TEXT)])
            else:
                new_code.extend([TextNode(element, text_type)])
            counter += 1
    return new_code