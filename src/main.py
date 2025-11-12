import os, shutil


def remove_public():
    path: str = './public'
    print(f'/public exists: {os.path.exists(path)}') # logging
    if os.path.exists(path):
        print(f'Removing everything at path: {path}') # logging
        shutil.rmtree(path)
    else:
        print('No "public" directory.') # logging

def copy_to_public(source='./content', destination='./public'):
    if not os.path.exists(destination):
        os.mkdir('./public')
    contents: list = os.listdir(source)
    print(f'Current dir contents: {contents}') # logging
    for content in contents:
        src: str = os.path.join(source, content)
        dst: str = os.path.join(destination, content)

        print(f'src: {src}\ndst: {dst}')
        if os.path.isfile(src):
            print(f'Copying to path: {dst}') # logging
            shutil.copy(src, dst)
        else:
            os.mkdir(dst)
            print(f'Recursion to: {src}') # logging
            copy_to_public(src, dst)


def main():
    remove_public()
    copy_to_public()


if __name__ == '__main__':
    main()
