class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None or self.props == {}:
            return ""
        new_props = ""
        for key in self.props:
            value = self.props[key]
            new_props = new_props + (f" {key}=\"{value}\"")
        return new_props
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        elif self.tag is None:
            return self.value
        else:
            new_props = self.props_to_html()
            return f"<{self.tag}{new_props}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("no tag")
        elif self.children is None:
            raise ValueError("no children")
        else:
            new_props = self.props_to_html()
            html_string = f"<{self.tag}{new_props}>"
            for child in self.children:
                html_string += child.to_html()
            html_string += f"</{self.tag}>"
        return html_string
    
            
            
        
    

    
