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
        curr = self.head
        is_completed = False
        while curr is not None:
            if curr.value == val and not is_completed:
                if prev_node is None:
                    next_node = curr.next
                    self.head = next_node
                    curr.next = None
                    curr = self.head
                else:
                    prev_node.next = curr.next
                    curr.next = None
                    curr = prev_node
                is_completed = not all and True
            else:
                prev_node = curr
                curr = curr.next
        self.tail = prev_node

    def clean(self):
        """Clean up current linked list"""
        node = self.head
        while node is not None:
            next_node = node.next
            node.next = None
            node = next_node

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

        if newNode.next == self.tail or afterNode == self.tail:
            self.tail = newNode
