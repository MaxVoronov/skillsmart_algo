import unittest
from src.bloom_filter import BloomFilter


class TestBloomFilter(unittest.TestCase):
    def setUp(self):
        self.bloom = BloomFilter(31)

    def tearDown(self):
        del self.bloom

    def test_hash1_function(self):
        self.assertEqual(24, self.bloom.hash1("0123456789"))
        self.assertEqual(12, self.bloom.hash1("5678901234"))
        self.assertEqual(6, self.bloom.hash1("8901234567"))
        self.assertEqual(0, self.bloom.hash1("BloomFilter"))

    def test_hash2_function(self):
        self.assertEqual(26, self.bloom.hash2("0123456789"))
        self.assertEqual(0, self.bloom.hash2("5678901234"))
        self.assertEqual(13, self.bloom.hash2("8901234567"))
        self.assertEqual(15, self.bloom.hash2("BloomFilter"))

    def test_add_check_value(self):
        # Generate cases and add to Bloom filter
        cases = []
        base = "0123456789"
        for i in range(0, 10):
            value = base[i:] + base[:i]
            cases.append(value)
            self.bloom.add(value)
        print(cases)

        # Test successful cases
        for case in cases:
            self.assertTrue(self.bloom.is_value(case))

        # Test non-exist cases
        self.assertFalse(self.bloom.is_value("HelloWorld!"))
        self.assertFalse(self.bloom.is_value("Fake value"))
        self.assertFalse(self.bloom.is_value("000000000"))
        self.assertFalse(self.bloom.is_value("no_data"))

        # Test false positive case
        self.assertTrue(self.bloom.is_value("111111111"))


if __name__ == '__main__':
    unittest.main()
