from textnode import TextNode
from website_functions import *
import os
import shutil
import sys

dir_path_static = "./static"
dir_path_public = "./docs"



def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for filename in os.listdir(dir_path_content):
        content_path = os.path.join(dir_path_content,filename)
        dest_path = os.path.join(dest_dir_path,filename)
        dest_path = dest_path.replace(".md", ".html")
        if os.path.isfile(content_path): 
            if filename.endswith(".md"):
                generate_page(content_path, template_path, dest_path, basepath)
        else:
            generate_pages_recursive(content_path, template_path, dest_path, basepath)

def main():
    if len(sys.argv)<2:
        basepath = "/"
    else:
        basepath = sys.argv[1]
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)
    generate_pages_recursive("./content", "./template.html", dir_path_public, basepath)

main()


    