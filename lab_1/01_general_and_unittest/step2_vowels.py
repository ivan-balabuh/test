import unittest

def count_vowels(text: str) -> int:
    vowels = "aeiouyаеєиіїоуюяAEIOUYАЕЄИІЇОУЮЯ"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

class TestCountVowels(unittest.TestCase):
    # Базові тести (⭐)
    def test_english_words(self):
        self.assertEqual(count_vowels("Hello World"), 3)
        self.assertEqual(count_vowels("Python"), 2)

    def test_uppercase_and_lowercase(self):
        self.assertEqual(count_vowels("AEIOUaeiou"), 10)

    def test_no_vowels(self):
        self.assertEqual(count_vowels("bcdfg"), 0)

    # Додаткові тести (🔥)
    def test_empty_string(self):
        self.assertEqual(count_vowels(""), 0)

    def test_numbers_and_symbols(self):
        self.assertEqual(count_vowels("12345!@#$%"), 0)

    def test_ukrainian_letters(self):
        self.assertEqual(count_vowels("Привіт, світе!"), 4)
        self.assertEqual(count_vowels("Єнот їсть яблуко"), 6)

if __name__ == "__main__":
    unittest.main(verbosity=2)