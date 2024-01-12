"""
    Create unit tests for the function fetch_ccc_paragraph()
    in fetch_catechism_of_the_catholic_church_paragraph.py
    To run the unit tests
        python3 test_unit.py
        pytest -k test_fetch_ccc_paragraph_invalid_9999
        pytest
"""

import unittest
from unittest.mock import patch

from fetch_catechism_of_the_catholic_church_paragraph import fetch_ccc_paragraph

class TestFetchCatechismOfTheCatholicChurchParagraph(unittest.TestCase):
    """
    Test the function fetch_ccc_paragraph() in fetch_catechism_of_the_catholic_church_paragraph.py
    """

    def test_fetch_ccc_paragraph_first(self):
        """
        Test fetch_ccc_paragraph() with a valid paragraph number
        """
        paragraph = 1
        expected = "God, infinitely perfect and blessed in himself,"
        self.assertIn(expected, fetch_ccc_paragraph(paragraph),
                      msg="Paragraph {paragraph} should contain '{expected}'")

    def test_fetch_ccc_paragraph_1111(self):
        """
        Test fetch_ccc_paragraph() with a valid paragraph number
        """
        paragraph = 1111
        expected = "Christ's work in the liturgy is sacramental:"
        self.assertIn(expected, fetch_ccc_paragraph(paragraph),
                      msg="Paragraph {paragraph} should contain '{expected}'")

    def test_fetch_ccc_paragraph_2222(self):
        """
        Test fetch_ccc_paragraph() with a valid paragraph number
        """
        paragraph = 2222
        expected = "Parents must regard their children as children of God"
        self.assertIn(expected, fetch_ccc_paragraph(paragraph),
                      msg="Paragraph {paragraph} should contain '{expected}'")

    def test_fetch_ccc_paragraph_last(self):
        """
        Test fetch_ccc_paragraph() with a valid paragraph number
        """
        paragraph = 2865
        expected = 'By the final "Amen," we express our "fiat" concerning the seven petitions: "So be it".'
        self.assertIn(expected, fetch_ccc_paragraph(paragraph),
                      msg="Paragraph {paragraph} should contain '{expected}, received {received}'")

    def test_fetch_ccc_paragraph_invalid_2857(self):
        """
        Test fetch_ccc_paragraph() with an invalid paragraph number
        """
        paragaph = 2866
        expected = "Paragraph 2866 not found."
        self.assertEqual(fetch_ccc_paragraph(paragaph), expected,
                         msg="Paragraph {paragraph} should not be found.")

    def test_fetch_ccc_paragraph_invalid_9999(self):
        """
        Test fetch_ccc_paragraph() with an invalid paragraph number
        """
        paragraph = 9999
        expected = "Paragraph 9999 not found."
        self.assertEqual(fetch_ccc_paragraph(paragraph), expected,
                         msg="Paragraph {paragraph} should not be found.")

    def test_fetch_ccc_paragraph_not_integer(self):
        """
        Test fetch_ccc_paragraph() with a non-integer
        """
        self.assertRaises(TypeError, fetch_ccc_paragraph, "abc")


if __name__ == '__main__':
    unittest.main()


