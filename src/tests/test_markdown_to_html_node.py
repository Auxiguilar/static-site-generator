import unittest

from src.functions import *


class TestMDToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_multiple(self):
        text = ("## header2\n\na paragraph of text; **look!**\nand _here!_\n\n```\n# and my code is **broken**!\nprint('help'!)\n```\n\n1. my imports are messed up for some reason\n2. I don't know _why_!\n\n- another\n- list")
        node = markdown_to_html_node(text)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>header2</h2><p>a paragraph of text; <b>look!</b> and <i>here!</i></p><pre><code># and my code is **broken**!\nprint('help'!)\n</code></pre><ol><li>my imports are messed up for some reason</li><li>I don't know <i>why</i>!</li></ol><ul><li>another</li><li>list</li></ul></div>",
        )
