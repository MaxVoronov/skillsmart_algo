import unittest
from src.dynamic_array import DynArray


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.arr = DynArray()

    def tearDown(self):
        del self.arr

    def test_insert_into_empty(self):
        self.arr.insert(0, 0)
        self.arr.insert(1, 10)

        self.assertEqual(0, self.arr[0])
        self.assertEqual(10, self.arr[1])
        self.assertEqual(16, self.arr.capacity)
        self.assertEqual(2, self.arr.count)

    def test_insert(self):
        self.arr.append(10)     # 10
        self.arr.insert(0, 0)   # 0 10
        self.arr.append(20)     # 0 10 20
        self.arr.append(40)     # 0 10 20 40
        self.arr.insert(3, 30)  # 0 10 20 30 40

        self.assertEqual(0, self.arr[0])
        self.assertEqual(10, self.arr[1])
        self.assertEqual(20, self.arr[2])
        self.assertEqual(30, self.arr[3])
        self.assertEqual(40, self.arr[4])
        self.assertRaises(IndexError, self.arr.__getitem__, 5)
        self.assertEqual(16, self.arr.capacity)
        self.assertEqual(5, self.arr.count)

    def test_insert_into_tail(self):
        self.arr.append(0)
        self.arr.append(10)
        self.arr.insert(self.arr.count, 20)

        self.assertEqual(0, self.arr[0])
        self.assertEqual(10, self.arr[1])
        self.assertEqual(20, self.arr[2])
        self.assertEqual(16, self.arr.capacity)
        self.assertEqual(3, self.arr.count)

    def test_insert_out_of_size(self):
        for i in range(64):
            self.arr.insert(i, i * 10)

        for i in range(64):
            self.assertEqual(i * 10, self.arr[i])
        self.assertEqual(64, self.arr.capacity)
        self.assertEqual(64, self.arr.count)

    def test_insert_invalid_index(self):
        self.arr.append(10)

        self.assertEqual(10, self.arr[0])
        self.assertRaises(IndexError, self.arr.__getitem__, -1)
        self.assertRaises(IndexError, self.arr.__getitem__, 1)
        self.assertRaises(IndexError, self.arr.insert, 3, 30)

    def test_delete(self):
        self.arr.append(0)
        self.arr.append(10)
        self.arr.append(20)
        self.arr.delete(1)

        self.assertEqual(0, self.arr[0])
        self.assertEqual(20, self.arr[1])
        self.assertRaises(IndexError, self.arr.__getitem__, 2)
        self.assertEqual(16, self.arr.capacity)
        self.assertEqual(2, self.arr.count)

    def test_delete_resizing(self):
        for i in range(18):  # From 0 to 17
            self.arr.append(i)
        self.assertEqual(32, self.arr.capacity)  # Increase 16 * 2
        self.assertEqual(18, self.arr.count)

        self.arr.delete(0)  # Remove 0 elem
        self.assertEqual(1, self.arr[0])
        self.assertEqual(32, self.arr.capacity)  # Capacity still equal 32
        self.assertEqual(17, self.arr.count)

        for i in range(9, 2, -1):  # Remove elements from 4 to 10 (values)
            self.arr.delete(i)
        self.assertEqual(1, self.arr[0])
        self.assertEqual(3, self.arr[2])
        self.assertEqual(11, self.arr[3])
        self.assertEqual(17, self.arr[self.arr.count - 1])
        self.assertEqual(21, self.arr.capacity)  # Capacity will reduced 32 / 1.5 = 21
        self.assertEqual(10, self.arr.count)

    def test_delete_invalid_index(self):
        self.assertRaises(IndexError, self.arr.delete, -1)
        self.assertRaises(IndexError, self.arr.delete, 0)

        for i in range(10):
            self.arr.append(i * 10)
        self.assertRaises(IndexError, self.arr.delete, -1)
        self.assertRaises(IndexError, self.arr.delete, 10)
        self.assertRaises(IndexError, self.arr.delete, 99)
