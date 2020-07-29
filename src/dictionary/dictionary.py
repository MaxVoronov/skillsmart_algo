class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        bytes_sum = 0
        for b in bytearray(key, 'utf-8'):
            bytes_sum += int(b)

        return bytes_sum % self.size

    def is_key(self, key):
        return key in self.slots

    def put(self, key, value):
        key_hash = self.hash_fun(key)
        self.slots[key_hash] = key
        self.values[key_hash] = value

    def get(self, key):
        if not self.is_key(key):
            return None
        idx = self.slots.index(key)

        return self.values[idx]
