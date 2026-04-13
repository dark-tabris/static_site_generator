from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
        if text_node.text_type == TextType.TEXT:
            return LeafNode(None, text_node.text)
        elif text_node.text_type == TextType.BOLD:
            return LeafNode("b", text_node.text)
        elif text_node.text_type == TextType.ITALIC:
            return LeafNode("i", text_node.text)
        elif text_node.text_type == TextType.CODE:
            return LeafNode("code", text_node.text)
        elif text_node.text_type == TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        elif text_node.text_type == TextType.IMAGE:
            return LeafNode("img", "", {"alt": text_node.text, "src": text_node.url})
        else:
            raise Exception("Undefined text type")

def block_to_block_type(text_block):
    lines = text_block.split("\n")

    if text_block[:4] == "```\n" and text_block[-3:] == "```":
        return BlockType.CODE

    if text_block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING

    is_quote = True
    for line in lines:
        if not line.startswith(">"):
            is_quote = False
            break

    is_unordered = True
    for line in lines:    
        if not line.startswith("- "):
            is_unordered = False
            break

    is_ordered = True
    i=1
    for line in lines:
        if not line.startswith(f"{i}. "):
            is_ordered = False
            break
        i += 1


    if is_quote:
        return BlockType.QUOTE
    elif is_unordered:
        return BlockType.UNORDERED_LIST
    elif is_ordered:
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH

        
    
    
