"""Simple unit testing
"""

import unittest
import cap

class TestCap(unittest.TestCase):
    def test_single_word(self):
        txt = "python"
        result = cap.cap_text(txt)
        self.assertEqual(result, "Python")
