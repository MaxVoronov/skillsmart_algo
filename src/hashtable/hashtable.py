class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        bytes_sum = 0
        for b in bytearray(value, 'utf-8'):
            bytes_sum += int(b)

        return bytes_sum % self.size

    def seek_slot(self, value):
        idx = self.hash_fun(value)
        slot_value = self.slots[idx]
        if slot_value is None:
            return idx

        i = 0
        while i < self.size:
            idx += self.step
            if idx > self.size - 1:
                idx -= self.size
            i += 1

            if self.slots[idx] is None:
                return idx

        return None

    def put(self, value):
        idx = self.seek_slot(value)
        if idx is not None:
            self.slots[idx] = value
            return idx

        return None

    def find(self, value):
        idx = self.hash_fun(value)
        slot_value = self.slots[idx]
        if slot_value == value:
            return idx

        i = 0
        while i < self.size:
            idx += self.step
            if idx > self.size - 1:
                idx -= self.size
            i += 1

            if self.slots[idx] == value:
                return idx

        return None
