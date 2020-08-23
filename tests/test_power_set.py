import unittest
from src.power_set import PowerSet


class TestPowerSet(unittest.TestCase):
    def setUp(self):
        self.storage = PowerSet()
        self.storage2 = PowerSet()

    def tearDown(self):
        del self.storage
        del self.storage2

    def test_common(self):
        self.storage.put(123)
        self.storage.put(234)
        self.storage.put(345)
        self.storage.put(345)  # Try to add existing element

        self.assertEqual(3, self.storage.size())
        self.assertTrue(self.storage.get(123))
        self.assertTrue(self.storage.get(234))
        self.assertTrue(self.storage.get(345))

        self.storage.remove(234)
        self.assertEqual(2, self.storage.size())
        self.assertTrue(self.storage.get(123))
        self.assertFalse(self.storage.get(234))
        self.assertTrue(self.storage.get(345))

    def test_union(self):
        self.storage.put(123)
        self.storage.put(234)

        # Union with empty set
        union = self.storage.union(self.storage2)
        self.assertEqual(2, self.storage.size())
        self.assertEqual(0, self.storage2.size())
        self.assertEqual(2, union.size())
        self.assertEqual([123, 234], union.storage)

        # Union with non empty set
        self.storage2.put(234)
        self.storage2.put(456)
        union = self.storage.union(self.storage2)
        self.assertEqual(2, self.storage.size())
        self.assertEqual(2, self.storage2.size())
        self.assertEqual(3, union.size())
        self.assertEqual([123, 234, 456], union.storage)

    def test_intersection(self):
        self.storage.put(123)
        self.storage.put(234)
        self.storage.put(345)
        self.storage2.put(456)

        intersection = self.storage.intersection(self.storage2)
        self.assertEqual(3, self.storage.size())
        self.assertEqual(1, self.storage2.size())
        self.assertEqual(0, intersection.size())
        self.assertEqual([], intersection.storage)

        self.storage2.put(234)
        self.storage2.put(345)
        intersection = self.storage.intersection(self.storage2)
        self.assertEqual(3, self.storage2.size())
        self.assertEqual(2, intersection.size())
        self.assertEqual([234, 345], intersection.storage)

    def test_difference(self):
        self.storage.put(123)
        self.storage.put(234)
        self.storage2.put(234)
        self.storage2.put(456)

        difference = self.storage.difference(self.storage2)
        self.assertEqual(2, self.storage.size())
        self.assertEqual(2, self.storage2.size())
        self.assertEqual(2, difference.size())
        self.assertEqual([123, 456], difference.storage)

    def test_issubset_case1(self):
        self.storage.put(123)
        self.storage.put(234)
        self.storage.put(456)
        self.storage2.put(123)
        self.storage2.put(456)
        self.assertEqual(3, self.storage.size())
        self.assertEqual(2, self.storage2.size())
        self.assertTrue(self.storage.issubset(self.storage2))

    def test_issubset_case2(self):
        self.storage.put(123)
        self.storage.put(234)
        self.storage2.put(123)
        self.storage2.put(234)
        self.storage2.put(567)
        self.assertEqual(2, self.storage.size())
        self.assertEqual(3, self.storage2.size())
        self.assertFalse(self.storage.issubset(self.storage2))

    def test_issubset_case3(self):
        self.storage.put(123)
        self.storage.put(234)
        self.storage.put(456)
        self.storage2.put(123)
        self.storage2.put(456)
        self.storage2.put(567)
        self.assertEqual(3, self.storage.size())
        self.assertEqual(3, self.storage2.size())
        self.assertFalse(self.storage.issubset(self.storage2))


if __name__ == '__main__':
    unittest.main()
