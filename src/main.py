import os, shutil, sys
from functions import generate_page


def remove_public():
    path: str = './public'
    print(f'RP > /public exists: {os.path.exists(path)}') # logging
    if os.path.exists(path):
        print(f'RP > Removing everything at path: {path}') # logging
        shutil.rmtree(path)
    else:
        print('RP > No "public" directory.') # logging

def copy_to_public(source='./content', destination='./public'):
    if not os.path.exists(destination):
        os.mkdir(destination)
    contents: list = os.listdir(source)
    print(f'CTP > Current dir contents: {contents}') # logging
    for content in contents:
        src: str = os.path.join(source, content)
        dst: str = os.path.join(destination, content)

        print(f'CTP > src: {src}\ndst: {dst}')
        if os.path.isfile(src):
            print(f'CTP > Copying to path: {dst}') # logging
            shutil.copy(src, dst)
        else:
            os.mkdir(dst)
            print(f'CTP > Recursion to: {src}') # logging
            copy_to_public(src, dst)

def generate_page_recursive(from_path: str, template_path: str, dest_path: str, basepath: str):
    contents: list = os.listdir(basepath + from_path)
    print(f'GPR > Current dir contents: {contents}') # logging
    for content in contents:
        src: str = os.path.join(basepath + from_path, content)
        dst: str = os.path.join(basepath + dest_path, content)

        print(f'GPR >\nsrc: {src}\ndst: {dst}')
        if not os.path.isfile(src):
            print(f'GPR > Recursion to: {src}') # logging
            generate_page_recursive(src, template_path, dst, basepath)
        elif os.path.isfile(src) and src.endswith('.md'):
            html_dst: str = dst.replace('.md', '.html') 
            print(f'GPR > Generating HTML page from {src} to {html_dst}:') # logging
            generate_page(src, template_path, html_dst, basepath)
        else:
            continue


def main(basepath: str = './'):
    remove_public()
    copy_to_public(source='content', destination='docs')
    generate_page_recursive('content', 'template.html', 'docs', basepath)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        main()
    else:
        main(sys.argv[1])
