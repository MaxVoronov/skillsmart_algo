from src.double_linked_list import LinkedList2, Node


class Stack:
    def __init__(self):
        self.stack = LinkedList2()

    def size(self):
        return self.stack.len()

    def push(self, value):
        node = Node(value)
        self.stack.add_in_head(node)

    def pop(self):
        if self.stack.len() > 0 and self.stack.head is not None:
            value = self.stack.head.value
            self.stack.delete(value)
            return value
        return None

    def peek(self):
        if self.stack.len() > 0 and self.stack.head is not None:
            return self.stack.head.value
        return None
