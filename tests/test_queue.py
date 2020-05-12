import unittest
from src.queue import Queue


class TestQueue(unittest.TestCase):
    def test_enqueue_dequeue(self):
        queue = Queue()
        values = [10, 20, 30, 40, 50]
        for value in values:
            queue.enqueue(value)

        self.assertEqual(len(values), queue.size())
        for value in values:
            self.assertEqual(value, queue.dequeue())
        self.assertEqual(0, queue.size())

    def test_enqueue_dequeue_big(self):
        queue = Queue()
        for i in range(10000):
            queue.enqueue(i + 1)

        for i in range(10000):
            queue.enqueue(queue.dequeue())

        self.assertEqual(10000, queue.size())

    def test_dequeue_empty(self):
        queue = Queue()
        self.assertIsNone(queue.dequeue())

    def test_rotate(self):
        # Format: Key - offset, value - expected state
        cases = {
            1: [20, 30, 40, 50, 60, 10],
            3: [40, 50, 60, 10, 20, 30],
            8: [30, 40, 50, 60, 10, 20],
            -1: [60, 10, 20, 30, 40, 50],
            -2: [50, 60, 10, 20, 30, 40],
            0: [10, 20, 30, 40, 50, 60],
            12: [10, 20, 30, 40, 50, 60],
        }
        for offset in cases.keys():
            queue = Queue()
            values = [10, 20, 30, 40, 50, 60]
            for value in values:
                queue.enqueue(value)
            queue.rotate(offset)

            expected_values = cases[offset]
            self.assertEqual(len(values), queue.size())
            for value in expected_values:
                self.assertEqual(value, queue.dequeue())


if __name__ == '__main__':
    unittest.main()
