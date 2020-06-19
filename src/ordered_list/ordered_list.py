class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self._ascending = asc

    def compare(self, v1, v2):
        if (self._ascending and v1 < v2) or (not self._ascending and v1 > v2):
            return -1
        if (self._ascending and v1 > v2) or (not self._ascending and v1 < v2):
            return 1
        return 0

    def add(self, value):
        prev = None
        curr = self.head
        while curr is not None:
            if self.compare(curr.value, value) > 0:
                self.insert_before(curr, Node(value))
                return
            prev = curr
            curr = curr.next
        self.insert(prev, Node(value))

    def add_in_head(self, newNode):
        if self.head is not None:
            newNode.next = self.head
            self.head.prev = newNode
        if self.tail is None:
            self.tail = newNode
        self.head = newNode

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def insert_before(self, beforeNode, newNode):
        if beforeNode is None or beforeNode.prev is None:
            self.add_in_head(newNode)
        else:
            beforeNode.prev.next = newNode
            newNode.prev = beforeNode.prev
            beforeNode.prev = newNode
            newNode.next = beforeNode

    def insert(self, afterNode, newNode):
        if afterNode is None or afterNode.next is None:
            self.add_in_tail(newNode)
        else:
            afterNode.next.prev = newNode
            newNode.next = afterNode.next
            afterNode.next = newNode
            newNode.prev = afterNode

    def find(self, val):
        curr = self.head
        while curr is not None:
            if self.compare(curr.value, val) == 0:
                return curr
            elif self.compare(curr.value, val) > 0:
                break
            curr = curr.next
        return None

    def delete(self, val):
        curr = self.head
        while curr is not None:
            if self.compare(curr.value, val) == 0:
                node = curr
                if curr.prev is None:
                    self.head = curr.next
                    if curr.next is not None:
                        curr.next.prev = None
                    curr = self.head
                else:
                    curr.prev.next = curr.next
                    curr = curr.prev

                if curr is None:
                    self.head = None
                    self.tail = None
                    continue
                elif curr.next is None:
                    self.tail = curr
                else:
                    curr.next.prev = curr

                node.prev = None
                node.next = None
                return
            elif self.compare(curr.value, val) > 0:
                return
            curr = curr.next

    def clean(self, asc):
        self._ascending = asc
        node = self.head
        while node is not None:
            next_node = node.next
            node.prev = None
            node.next = None
            node = next_node
        self.head = None
        self.tail = None

    def len(self):
        result = 0
        node = self.head
        while node is not None:
            node = node.next
            result += 1
        return result

    def get_all(self):
        r = []
        node = self.head
        while node is not None:
            r.append(node)
            node = node.next
        return r

    def print(self):
        print("\n[H]", end=' <-> ')
        node = self.head
        while node is not None:
            print('[' + str(node.value) + ']', end=' <-> ')
            node = node.next
        print("[T]")


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        v1 = v1.strip()
        v2 = v2.strip()
        if (self._ascending and v1 < v2) or (not self._ascending and v1 > v2):
            return -1
        if (self._ascending and v1 > v2) or (not self._ascending and v1 < v2):
            return 1
        return 0
