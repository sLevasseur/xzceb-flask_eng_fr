import unittest
from translator import english_to_french, french_to_english

class TestTranslation(unittest.TestCase):
    def testEnglishToFrench(self):
        self.assertEqual(english_to_french("How are you?"), "Comment es-tu?")



unittest.main()
