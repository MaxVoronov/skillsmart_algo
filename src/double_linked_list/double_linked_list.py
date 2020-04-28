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
        If *afterNode* is None, then new node will added into tail
        """
        if afterNode is None or afterNode.next is None:
            self.add_in_tail(newNode)
        else:
            afterNode.next.prev = newNode
            newNode.next = afterNode.next
            afterNode.next = newNode
            newNode.prev = afterNode

    def add_in_head(self, newNode):
        """
        Insert node into list head
        """
        if self.head is not None:
            newNode.next = self.head
            self.head.prev = newNode
        if self.tail is None:
            self.tail = newNode
        self.head = newNode

    def print(self):
        """
        Print linked list (for debug)
        """
        print("\n[H]", end=' <-> ')
        node = self.head
        while node is not None:
            print('[' + str(node.value) + ']', end=' <-> ')
            node = node.next
        print("[T]")
