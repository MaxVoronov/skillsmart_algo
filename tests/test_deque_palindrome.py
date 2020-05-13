import unittest
from src.deque import Deque


class TestDequePalindrome(unittest.TestCase):
    palindrome_cases = [
        '',       # Empty sentence
        'level',  # Include non-pair char in middle
        'Anna',   # Without non-pair char
        'refer',
        'Renner',
        'Step on no pets',
        'Madam, I\'m Adam',  # Exclude any special chars and spaces
        'Mr. Owl ate my metal worm',
        'Rats live on no evil star',
    ]
    non_palindrome_cases = [
        'hello',
        'Palindromes',
        'Lorem ipsum dolor sit amet',
    ]

    @staticmethod
    def is_palindrome(sentence):
        dq = Deque()
        sentence = ''.join(filter(str.isalnum, sentence.lower()))
        for char in sentence:
            dq.addFront(char)

        while dq.size() > 1:
            if dq.removeFront() != dq.removeTail():
                return False
        return True

    def test_palindromes(self):
        for sentence in self.palindrome_cases:
            self.assertTrue(self.is_palindrome(sentence))

    def test_non_palindromes(self):
        for sentence in self.non_palindrome_cases:
            self.assertFalse(self.is_palindrome(sentence))


if __name__ == '__main__':
    unittest.main()
