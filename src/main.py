import functions, htmlnode, textnode


def main():
    text = ("## header2\n\na paragraph of text; **look!**\nand _here!_\n\n```\n# and my code is **broken**!\nprint('help'!)\n```\n\n1. my imports are fucked for some reason\n2. I don't know _why_!\n\n- another\n- list")
    node = functions.markdown_to_html_node(text)
    print(node.to_html())


if __name__ == '__main__':
    main()
