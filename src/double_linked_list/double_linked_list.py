class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        """Add new node to end of linked list"""
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

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
        curr = self.head
        is_completed = False
        while curr is not None:
            if curr.value == val and not is_completed:
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

                is_completed = not all and True
            else:
                curr = curr.next

    def clean(self):
        """Clean up current linked list"""
        node = self.head
        while node is not None:
            next_node = node.next
            node.prev = None
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
            newNode.prev = None
            newNode.next = self.head
            self.head = newNode
        else:
            newNode.prev = afterNode
            newNode.next = afterNode.next
            if afterNode.next is not None:
                afterNode.next.prev = newNode
            afterNode.next = newNode

        if newNode.next == self.tail or afterNode == self.tail:
            self.tail = newNode

    def add_in_head(self, newNode):
        """
        Insert node into list head
        """
        self.insert(None, newNode)
