import unittest
from src.hashtable import HashTable


class TestHashTable(unittest.TestCase):
    cases = {
        "Hello": 6,
        "Cat": 14,
        "Tiger": 13,
        "Duck": 11,
        "Lion": 3,
        "Pig": 3,
        "Long sentence with special symbol!": 8,
    }

    def setUp(self):
        self.storage = HashTable(19, 3)

    def tearDown(self):
        del self.storage

    def test_hash_function(self):
        for word in self.cases:
            expected_hash = self.cases[word]
            actual_hash = self.storage.hash_fun(word)
            self.assertEqual(expected_hash, actual_hash)

    def test_seek_slot(self):
        # Test empty slots
        self.assertEqual(3, self.storage.seek_slot("Lion"))
        self.assertEqual(13, self.storage.seek_slot("Tiger"))

        # Test occupied slots
        self.storage.slots[13] = "Fake"
        self.storage.slots[14] = "Fake"
        self.assertEqual(17, self.storage.seek_slot("Cat"))  # Hash: 14 + 1 step
        self.assertEqual(16, self.storage.seek_slot("Tiger"))  # Hash: 13 + 1 step
        self.storage.slots[11] = "Fake"
        self.storage.slots[17] = "Fake"
        self.assertEqual(1, self.storage.seek_slot("Duck"))  # Hash: 11 + 2 steps

        # Test when all slots are occupied
        for idx in range(self.storage.size):
            self.storage.slots[idx] = "Fake"
        self.assertIsNone(self.storage.seek_slot("Hello"))

    def test_put(self):
        # Test put in empty slots
        self.assertEqual(3, self.storage.put("Lion"))
        self.assertEqual(self.storage.slots[3], "Lion")
        self.assertEqual(13, self.storage.put("Tiger"))
        self.assertEqual(self.storage.slots[13], "Tiger")

        # Test put in occupied slot
        self.assertEqual(6, self.storage.put("Pig"))  # Hash: 3
        self.assertEqual(self.storage.slots[6], "Pig")

        # Test when all slots are occupied
        for idx in range(self.storage.size):
            self.storage.slots[idx] = "Fake"
        self.assertIsNone(self.storage.put("Duck"))
        for idx in range(self.storage.size):
            self.assertEqual("Fake", self.storage.slots[idx])

    def test_find(self):
        # Add some data to slots
        for word in self.cases:
            self.storage.put(word)

        # Test usual cases
        self.assertEqual(13, self.storage.find("Tiger"))
        self.assertEqual(14, self.storage.find("Cat"))
        self.assertEqual(11, self.storage.find("Duck"))

        # Test cases with collision
        self.assertEqual(3, self.storage.find("Lion"))  # Hash: 3
        self.assertEqual(6, self.storage.find("Hello"))  # Hash: 6
        self.assertEqual(9, self.storage.find("Pig"))  # Hash: 3 + collision (idx 3 and 6)


if __name__ == '__main__':
    unittest.main()
