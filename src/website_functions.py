import shutil
import os
from htmlnode import *
from textnode import *
from markup import markdown_to_html_node



def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)

def extract_title(markdown):
    split_text = markdown.split("\n")
    for line in split_text:
        line = line.strip()
        if line.startswith(("# ")):
            return line[2:]
    raise Exception("No Header")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    f = open(from_path)
    markdown_file = f.read()
    f.close
    f = open(template_path)
    temp = f.read()
    f.close
    html_string = (markdown_to_html_node(markdown_file)).to_html()
    title = extract_title(markdown_file)
    file_output = temp.replace("{{ Content }}", html_string).replace("{{ Title }}", title)
    if not os.path.exists(dest_path):
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    f = open(dest_path, 'w+')
    f.write(file_output)        
    f.close

