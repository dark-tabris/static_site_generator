import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for individual_node in old_nodes:
        if individual_node.text_type is not TextType.TEXT:
            new_nodes.append(individual_node)
        elif individual_node.text.count(delimiter)% 2 != 0:
            raise Exception("Invalid Markdown Syntax")
        else:
            text_in_individual_node_split_list = individual_node.text.split(delimiter)
            for i in range(0, len(text_in_individual_node_split_list)):
                if i % 2 == 0:
                    if text_in_individual_node_split_list[i] != "":
                        new_nodes.append(TextNode(text_in_individual_node_split_list[i], individual_node.text_type))
                else:
                    if text_in_individual_node_split_list[i] != "":
                        new_nodes.append(TextNode(text_in_individual_node_split_list[i], text_type))
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for individual_node in old_nodes:
        if individual_node.text_type != TextType.TEXT:
            new_nodes.append(individual_node)
            continue
        images = extract_markdown_images(individual_node.text)
        if not images:
            if individual_node.text != "":
                new_nodes.append(individual_node)
        else:
            original_text = individual_node.text
            for image in images:
                image_alt, image_link = image
                sections = original_text.split(f"![{image_alt}]({image_link})", 1)
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
                original_text = sections[1]
            if original_text != "":
                new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for individual_node in old_nodes:
        if individual_node.text_type != TextType.TEXT:
            new_nodes.append(individual_node)
            continue
        links = extract_markdown_links(individual_node.text)
        if not links:
            if individual_node.text != "":
                new_nodes.append(individual_node)
        else:
            original_text = individual_node.text
            for link in links:
                link_text, link_link = link
                sections = original_text.split(f"[{link_text}]({link_link})", 1)
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(link_text, TextType.LINK, link_link))
                original_text = sections[1]
            if original_text != "":
                new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

        
def text_to_textnodes(text):
    new_nodes = [TextNode(text, TextType.TEXT)]
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    new_nodes = split_nodes_image(new_nodes)  
    new_nodes = split_nodes_link(new_nodes)   
    return new_nodes

def markdown_to_blocks(markdown):
    filtered_blocks = []
    block_list = markdown.split("\n\n")
    for block in block_list:
        if block:
            filtered_blocks.append(block.strip())
    return filtered_blocks





