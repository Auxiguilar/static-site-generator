import unittest
from src.functions import extract_title


class TestTitleExtraction(unittest.TestCase):
    def test_correct_title(self):
        markdown: str = '''# The title

The rest!
'''
        title: str = extract_title(markdown)
        self.assertEqual(title, 'The title')

    def test_incorrect_title(self):
        markdown: str = '''## The title

The rest!
'''
        with self.assertRaises(Exception):
            title: str = extract_title(markdown)

    def test_no_title(self):
        markdown: str = '''The title

The rest!
'''
        with self.assertRaises(Exception):
            title: str = extract_title(markdown)

