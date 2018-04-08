"""Simple unit testing
"""

import unittest
import cap

class TestCap(unittest.TestCase):
    def test_single_word(self):
        txt = "python"
        result = cap.cap_text(txt)
        self.assertEqual(result, "Python")

    def test_multiple_words(self):
        txt = "first second third"
        result = cap.cap_text(txt)
        self.assertEqual(result, "First Second Third")
