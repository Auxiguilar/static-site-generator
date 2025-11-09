import unittest

from src.functions import block_to_blocktype, BlockType # ??? interesting...

# or: if something goes wrong, rewrite your .md; not my problem!
class TestToBlocktype(unittest.TestCase):
    def test_paragraph(self):
        block: str = 'paragraph!'
        block_type: BlockType = block_to_blocktype(block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_heading(self):
        block: str = '### heading!'
        block_type: BlockType = block_to_blocktype(block)
        self.assertEqual(BlockType.HEADING, block_type)

    def test_code(self):
        block: str = '```code!```'
        block_type: BlockType = block_to_blocktype(block)
        self.assertEqual(BlockType.CODE, block_type)

    def test_quote(self):
        block: str = '>quote!\n>and more quote!'
        block_type: BlockType = block_to_blocktype(block)
        self.assertEqual(BlockType.QUOTE, block_type)

    def test_unordered_list(self):
        block: str = '- item\n- another item\n- and another!'
        block_type: BlockType = block_to_blocktype(block)
        self.assertEqual(BlockType.UNORDERED_LIST, block_type)

    def test_ordered_list(self):
        block: str = '1. item\n2. another item\n3. and another!'
        block_type: BlockType = block_to_blocktype(block)
        self.assertEqual(BlockType.ORDERED_LIST, block_type)
