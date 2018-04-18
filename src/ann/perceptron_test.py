import unittest
from .perceptron import Perceptron

class CardTest(unittest.TestCase):
    def test_feeding(self):
        perc = Perceptron(3)
        perc.feed([1,2,3]).activate()
        print(perc)
