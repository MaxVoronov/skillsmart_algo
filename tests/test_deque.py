import unittest
from src.deque import Deque


class TestDeque(unittest.TestCase):
    def setUp(self):
        self.dq = Deque()

    def tearDown(self):
        del self.dq

    def test_add_remove_front(self):
        values = list(range(10000))
        for value in values:
            self.dq.addFront(value)

        self.assertEqual(len(values), self.dq.size())
        values.reverse()
        for value in values:
            self.assertEqual(value, self.dq.removeFront())
        self.assertEqual(0, self.dq.size())

    def test_add_remove_tail(self):
        values = list(range(10000))
        for value in values:
            self.dq.addTail(value)

        self.assertEqual(len(values), self.dq.size())
        values.reverse()
        for value in values:
            self.assertEqual(value, self.dq.removeTail())
        self.assertEqual(0, self.dq.size())

    def test_add_tail_remove_front(self):
        values = list(range(10000))
        for value in values:
            self.dq.addTail(value)

        self.assertEqual(len(values), self.dq.size())
        for value in values:
            self.assertEqual(value, self.dq.removeFront())
        self.assertEqual(0, self.dq.size())

    def test_add_front_remove_tail(self):
        values = list(range(10000))
        for value in values:
            self.dq.addFront(value)

        self.assertEqual(len(values), self.dq.size())
        for value in values:
            self.assertEqual(value, self.dq.removeTail())
        self.assertEqual(0, self.dq.size())

    def test_remove_front_empty(self):
        self.assertIsNone(self.dq.removeFront())

    def test_remove_tail_empty(self):
        self.assertIsNone(self.dq.removeTail())

    def test_size_empty(self):
        self.assertEqual(0, self.dq.size())


if __name__ == '__main__':
    unittest.main()
