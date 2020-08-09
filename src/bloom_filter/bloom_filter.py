class BloomFilter:
    def __init__(self, f_len):
        self.filter_len = f_len
        self.data = [0] * self.filter_len
        # Use f_len (32bits) and max records (10)
        # Then: k = 0.6931 * (31 / 10) = 2.149 = 2
        # Therefore we need 2 hash function

    def hash1(self, str1):
        result = 0
        for c in str1:
            result = (result * 17 + ord(c)) % self.filter_len
        return result

    def hash2(self, str1):
        result = 0
        for c in str1:
            result = result * 223 + ord(c)
        return result % self.filter_len

    def add(self, str1):
        idx_hash_1 = self.hash1(str1)
        idx_hash_2 = self.hash2(str1)
        self.data[idx_hash_1] = 1
        self.data[idx_hash_2] = 1

    def is_value(self, str1):
        idx_hash_1 = self.hash1(str1)
        idx_hash_2 = self.hash2(str1)

        print(str1, idx_hash_1, self.data[idx_hash_1], idx_hash_2, self.data[idx_hash_2])

        return self.data[idx_hash_1] == 1 and self.data[idx_hash_2] == 1
