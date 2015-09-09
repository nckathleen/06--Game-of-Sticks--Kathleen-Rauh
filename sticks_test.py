import unittest
from sticks import *

class TestSticks(unittest.TestCase):


def sticks_taken():
    word = "integration"
    self.assertEqual(display_word(word, [4]), "_ _ _ _ _ _ _ _ _ _ _")
    self.assertEqual(display_word(word, ["z"]), "_ _ _ _ _ _ _ _ _ _ _")
    self.assertEqual(display_word(word, ["0"]), "_ _ _ _ G _ _ _ _ _ _")
    self.assertEqual(display_word(word, ["i"]), "I _ _ _ _ _ _ _ I _ _")
    self.assertEqual(display_word(word, ["i", "g"]), "I _ _ _ G _ _ _ I _ _")
    self.assertEqual(display_word(word, ["i", "n", "z"]), "I N _ _ _ _ _ _ I _ N")


def sticks_on_table():


def 
