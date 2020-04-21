class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        """Add new node to end of linked list"""
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        """Print all values one per line"""
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        """Try to find one node by value"""
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        """Try to find all nodes by value and return list"""
        result = []
        node = self.head
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def delete(self, val, all=False):
        """Remove one or all nodes with passed value"""
        prev_node = None
        node = self.head
        is_removed = False
        while node is not None:
            if node.value == val and not is_removed:
                if prev_node is None:
                    self.head = node.next
                else:
                    prev_node.next = node.next
                    node = prev_node
                if not all:
                    is_removed = True
            prev_node = node
            node = node.next
        self.tail = node

    def clean(self):
        """Clean up current linked list"""
        self.head = None
        self.tail = None

    def len(self):
        """Return length of linked list"""
        result = 0
        node = self.head
        while node is not None:
            node = node.next
            result += 1
        return result

    def insert(self, afterNode, newNode):
        """
        Insert node into linked list after another node
        If *afterNode* is None, then new node will added into head
        """
        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
        else:
            newNode.next = afterNode.next
            afterNode.next = newNode
