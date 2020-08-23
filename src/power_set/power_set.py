class PowerSet:
    def __init__(self):
        self.storage = []

    def put(self, value):
        if not self.get(value):
            self.storage.append(value)

    def get(self, value):
        return value in self.storage

    def remove(self, value):
        if self.get(value):
            self.storage.remove(value)
            return True
        return False

    def size(self):
        return len(self.storage)

    def union(self, set2):
        result = self.storage.copy()
        for value in set2.storage:
            if value not in result:
                result.append(value)
        return result

    def intersection(self, set2):
        result = []
        for value in set2.storage:
            if value in self.storage:
                result.append(value)
        return result

    def difference(self, set2):
        result = []
        for value in self.storage:
            if value not in set2.storage and value not in result:
                result.append(value)
        for value in set2.storage:
            if value not in self.storage and value not in result:
                result.append(value)
        return result

    def issubset(self, set2):
        if set2.size() > self.size():   # Optimization
            return False

        for value in set2.storage:
            if value not in self.storage:
                return False
        return True
