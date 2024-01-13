"""
    Create unit tests for the function fetch_ccc_paragraph()
    in skill_fetch_catechism_of_the_catholic_church_paragraph.py
    To run the unit tests
        python3 test_unit.py
        pytest -k test_fetch_ccc_paragraph_invalid_9999
        pytest
"""

import unittest
from unittest.mock import patch

from skill_fetch_catechism_of_the_catholic_church_paragraph import fetch_ccc_paragraph

class TestFetchCatechismOfTheCatholicChurchParagraph(unittest.TestCase):
    """
    Test the function fetch_ccc_paragraph() in skill_fetch_catechism_of_the_catholic_church_paragraph.py
    """

    def test_fetch_ccc_paragraph_first(self):
        """
        Test fetch_ccc_paragraph() with a valid paragraph number
        """
        paragraphs = [1]
        expected = "God, infinitely perfect and blessed in himself,"
        results = fetch_ccc_paragraph(paragraphs)
        self.assertIn(expected, results[0], msg=f"Paragraph {paragraphs} should contain '{expected}', \nReceived {results}")

    def test_fetch_ccc_paragraph_1111(self):
        """
        Test fetch_ccc_paragraph() with a valid paragraph number
        """
        paragraphs = [1111]
        expected = "Christ's work in the liturgy is sacramental:"
        results = fetch_ccc_paragraph(paragraphs)
        self.assertIn(expected, results[0], msg=f"Paragraph {paragraphs} should contain '{expected}', \nReceived {results}")

    def test_fetch_ccc_paragraph_2222(self):
        """
        Test fetch_ccc_paragraph() with a valid paragraph number
        """
        paragraphs = [2222]
        expected = "Parents must regard their children as children of God"
        results = fetch_ccc_paragraph(paragraphs)
        self.assertIn(expected, results[0], msg=f"Paragraph {paragraphs} should contain '{expected}', \nReceived {results}")

    def test_fetch_ccc_paragraph_last(self):
        """
        Test fetch_ccc_paragraph() with a valid paragraph number
        """
        paragraphs = [2865]
        expected = 'By the final "Amen," we express our "fiat" concerning the seven petitions: "So be it".'
        results = fetch_ccc_paragraph(paragraphs)
        self.assertIn(expected, results[0], msg=f"Paragraph {paragraphs} should contain '{expected}, \nReceived {results}'")

    def test_fetch_ccc_paragraph_invalid_2866(self):
        """
        Test fetch_ccc_paragraph() with an invalid paragraph number
        """
        paragraphs = [2866]
        expected = "Paragraph 2866 not found."
        results = fetch_ccc_paragraph(paragraphs)
        self.assertEqual( results[0], expected, msg=f"Paragraph {paragraphs} should not be found.")

    # test with multiple paragraphs
    def test_fetch_ccc_paragraph_multiple(self):
        """
        Test fetch_ccc_paragraph() with a valid paragraph number
        """
        paragraphs = [1, 1111, 2222, 2865]
        expecteds = []
        expecteds.append("God, infinitely perfect and blessed in himself,")
        expecteds.append("Christ's work in the liturgy is sacramental:")
        expecteds.append("Parents must regard their children as children of God")
        expecteds.append('By the final "Amen," we express our "fiat" concerning the seven petitions: "So be it".')

        results = fetch_ccc_paragraph(paragraphs)

        print(f"results: {results}\n\n")

        # loop over each of the paragraphs and get the paragraph number, and check that the expected text is in the results
        # if not found, print the paragraph number and the results expected and received
        for paragraph, expected in zip(paragraphs, expecteds):
            result = results[paragraphs.index(paragraph)]
            self.assertIn(expected, result, msg=f"Paragraph {paragraph} should contain '{expected}', INSTEAD, RECEIVED: '{results}'")



    def test_fetch_ccc_paragraph_invalid_9999(self):
        """
        Test fetch_ccc_paragraph() with an invalid paragraph number
        """
        paragraphs = [9999]
        expected = "Paragraph 9999 not found."
        results = fetch_ccc_paragraph(paragraphs)
        self.assertEqual( results[0], expected, msg=f"Paragraph {paragraphs} should not be found.")

    def test_fetch_ccc_paragraph_not_integer(self):
        """
        Test fetch_ccc_paragraph() with a non-integer
        """
        self.assertRaises(TypeError, fetch_ccc_paragraph, ["abc"])


if __name__ == '__main__':
    unittest.main()


