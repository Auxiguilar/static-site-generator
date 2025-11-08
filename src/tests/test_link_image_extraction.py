import unittest

from src.functions import extract_markdown_images, extract_markdown_links


class TestExtraction(unittest.TestCase):
    def test_image_extraction(self):
        text: str = 'This is a [link](links/link), and this is an ![image](images/image)'
        images: list[tuple] = extract_markdown_images(text)
        self.assertEqual(images[0][0], 'image')
        self.assertEqual(images[0][1], 'images/image')
        self.assertEqual(1, len(images))

    def test_link_extraction(self):
        text: str = 'This is a [link](links/link), and this is an ![image](images/image)'
        links: list[tuple] = extract_markdown_links(text)
        self.assertEqual(links[0][0], 'link')
        self.assertEqual(links[0][1], 'links/link')

    def test_multiple(self):
        text: str = '[link1](links/link1), [link2](links/link2), ![image1](images/image1)'
        images: list[tuple] = extract_markdown_images(text)
        self.assertEqual(1, len(images))
        links: list[tuple] = extract_markdown_links(text)
        self.assertEqual(2, len(links))
