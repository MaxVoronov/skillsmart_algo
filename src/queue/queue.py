class Queue:
    def __init__(self):
        self.read_queue = Stack()
        self.write_queue = Stack()

    def enqueue(self, item):
        self.write_queue.push(item)

    def dequeue(self):
        if self.read_queue.size() > 0:
            return self.read_queue.pop()

        if self.write_queue.size() > 0:
            while self.write_queue.size() > 0:
                self.read_queue.push(self.write_queue.pop())
            return self.read_queue.pop()

        return None

    def size(self):
        return self.read_queue.size() + self.write_queue.size()

    def rotate(self, offset):
        real_offset = (offset % self.size())  # Loop optimization
        while real_offset > 0:
            self.enqueue(self.dequeue())
            real_offset -= 1


# Dependencies
class Stack:
    def __init__(self):
        self.stack = LinkedList2()

    def size(self):
        return self.stack.len()

    def push(self, value):
        node = Node(value)
        self.stack.add_in_head(node)

    def pop(self):
        node = self.stack.first()
        if self.stack.len() > 0 and node is not None:
            self.stack.delete(node)
            return node.value
        return None

    def peek(self):
        if self.stack.len() > 0 and self.stack.head is not None:
            return self.stack.head.value
        return None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def first(self):
        return self.head

    def add_in_head(self, newNode):
        """Insert node into list head"""
        if self.head is not None:
            newNode.next = self.head
            self.head.prev = newNode
        if self.tail is None:
            self.tail = newNode
        self.head = newNode
        self.length += 1

    def delete(self, node):
        """Remove one or all nodes with passed value"""
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

        node.prev = None
        node.next = None
        self.length -= 1

    def len(self):
        """Return length of linked list"""
        return self.length


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None
