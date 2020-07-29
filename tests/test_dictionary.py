import unittest
from src.dictionary import NativeDictionary


class TestDictionary(unittest.TestCase):
    def setUp(self):
        self.storage = NativeDictionary(19)

    def tearDown(self):
        del self.storage

    def test_hash_func(self):
        cases = {"key1": 17, "key2": 18, "fake_key": 14, "12345": 8}
        for key in cases:
            expected_hash = cases[key]
            actual_hash = self.storage.hash_fun(key)
            self.assertEqual(expected_hash, actual_hash)

    def test_put_get(self):
        elem_count = 5
        self.populate_dict(self.storage, elem_count)

        for idx in range(1, elem_count + 1):
            self.assertEqual(idx, self.storage.get("key" + str(idx)))

    def test_is_key(self):
        elem_count = 5
        self.populate_dict(self.storage, elem_count)

        for idx in range(1, elem_count + 1):
            self.assertTrue(self.storage.is_key("key" + str(idx)))
        self.assertFalse(self.storage.is_key("key" + str(elem_count + 1)))
        self.assertFalse(self.storage.is_key("fake_key"))

    @staticmethod
    def populate_dict(dict, elem_count):
        for idx in range(1, elem_count + 1):
            dict.put("key" + str(idx), idx)


if __name__ == '__main__':
    unittest.main()
