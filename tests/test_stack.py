import unittest
from src.stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def tearDown(self):
        del self.stack

    def test_push_pop_peek(self):
        values = [10, 20, 30, 40, 50]
        for value in values:
            self.stack.push(value)

        self.assertEqual(len(values), self.stack.size())
        values.reverse()
        for value in values:
            self.assertEqual(value, self.stack.peek())
            self.assertEqual(value, self.stack.pop())

    def test_pop(self):
        self.stack.push(10)
        self.assertEqual(1, self.stack.size())
        self.assertEqual(10, self.stack.pop())
        self.assertEqual(0, self.stack.size())

    def test_peek(self):
        self.stack.push(10)
        self.assertEqual(1, self.stack.size())
        self.assertEqual(10, self.stack.peek())
        self.assertEqual(1, self.stack.size())

    def test_pop_empty(self):
        self.assertIsNone(self.stack.pop())

    def test_peek_empty(self):
        self.assertIsNone(self.stack.peek())


if __name__ == '__main__':
    unittest.main()
