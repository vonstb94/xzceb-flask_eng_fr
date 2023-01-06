import unittest

from translator import english_to_french, french_to_english

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self):
        self.assertEqual(french_to_english(''), '')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english(''), '')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
  


unittest.main()