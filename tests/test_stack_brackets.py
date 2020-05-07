import unittest
from src.stack import Stack


class TestStackBrackets(unittest.TestCase):
    @staticmethod
    def validate_brackets(sentence):
        brackets = Stack()
        for char in sentence:
            if char == '(':
                brackets.push(True)
            elif char == ')':
                if brackets.pop() is not True:
                    return False
        return brackets.size() == 0

    def test_correct_cases(self):
        self.assertTrue(self.validate_brackets(''))
        self.assertTrue(self.validate_brackets('()'))
        self.assertTrue(self.validate_brackets('()(())'))
        self.assertTrue(self.validate_brackets('(()((())()))'))
        self.assertTrue(self.validate_brackets('([23 + 4] * 5)'))
        self.assertTrue(self.validate_brackets('(81 / 9) + (55 - 12)'))

    def test_incorrect_cases(self):
        self.assertFalse(self.validate_brackets(')('))
        self.assertFalse(self.validate_brackets('(()))'))
        self.assertFalse(self.validate_brackets('(()()(()'))
        self.assertFalse(self.validate_brackets('())('))
        self.assertFalse(self.validate_brackets('))(('))
        self.assertFalse(self.validate_brackets('((())'))
        self.assertFalse(self.validate_brackets('(81 / 9) + (55 - 12))'))


if __name__ == '__main__':
    unittest.main()
