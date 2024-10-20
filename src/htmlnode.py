class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("Child classes will override this method to render themselves as HTML.")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        attr = ""
        for key, value in self.props.items():
            attr += f' {key}="{value}"'
        return attr
    
    
    def __repr__(self):
        return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        self.value = value
        self.tag = tag
        self.props = props
        
    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf nodes require a value")
        elif self.tag is None:
            return f"{self.value}"
        else:
            return (f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>")
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
