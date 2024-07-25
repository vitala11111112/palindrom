import unittest
import Palindrom
class TestPalindrom(unittest.TestCase):
    def setUp(self):
        self.obj = Palindrom.Palindrom()
    def test_find_longest_palindrome(self):
        self.assertEqual(self.obj.find_longest_palindrome(("babab")),"babab")
        self.assertEqual(self.obj.find_longest_palindrome(("baxgfbk")),"")
unittest.main()