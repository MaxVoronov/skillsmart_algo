import ctypes


class DynArray:
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def make_array(self, new_capacity):
        """Allocate new array in memory"""
        return (new_capacity * ctypes.py_object)()

    def resize(self, new_capacity):
        """Create new array with new capacity"""
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        """Append item to end of array"""
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        """Insert item by index"""
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')

        if self.count == self.capacity:
            self.resize(2 * self.capacity)

        for idx in range(self.count - 1, i - 1, -1):
            self.array[idx + 1] = self.array[idx]
        self.array[i] = itm
        self.count += 1

    def delete(self, i):
        """Remove item by index"""
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')

        capacity = self.capacity
        if self.count < self.capacity // 2:
            capacity = int(self.capacity / 1.5)
            # Min capacity = 16
            if capacity < 16:
                capacity = 16

        insert_idx = 0
        new_array = self.make_array(capacity)
        for idx in range(self.count):
            if idx == i:
                continue    # Skip removed element
            new_array[insert_idx] = self.array[idx]
            insert_idx += 1

        self.array = new_array
        self.capacity = capacity
        self.count = insert_idx

    def print(self):
        """Print array items (for debug)"""
        print()
        for idx, val in enumerate(self):
            print("- [" + str(idx) + "]: " + str(val))
