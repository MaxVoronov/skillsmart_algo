import unittest
from src.linked_list import LinkedList, Node


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()

    def tearDown(self):
        del self.list

    def test_add_in_tail(self):
        first_node = Node(23)
        second_node = Node(72)

        self.list.add_in_tail(first_node)
        self.assertEqual(first_node, self.list.head)
        self.assertEqual(first_node, self.list.tail)

        self.list.add_in_tail(second_node)
        self.assertEqual(first_node, self.list.head)
        self.assertEqual(second_node, self.list.tail)
        self.assertEqual(second_node, first_node.next)
        self.assertIsNone(second_node.next)

    def test_find(self):
        node = Node(99)
        self.list.add_in_tail(Node(13))
        self.list.add_in_tail(Node(0))
        self.list.add_in_tail(node)
        self.list.add_in_tail(Node(44))

        found_node = self.list.find(node.value)
        self.assertIsNotNone(found_node)
        self.assertEqual(node, found_node)

    def test_find_in_empty_list(self):
        node = Node(99)
        found_node = self.list.find(node.value)

        self.assertEqual(0, self.list.len())
        self.assertIsNone(found_node)

    def test_find_all(self):
        source_node = Node(99)
        self.list.add_in_tail(Node(28))
        self.list.add_in_tail(Node(source_node.value))
        self.populate_list(self.list)
        self.list.add_in_tail(Node(source_node.value))
        self.list.add_in_tail(Node(81))
        self.list.add_in_tail(source_node)

        found_nodes = self.list.find_all(source_node.value)
        self.assertEqual(3, len(found_nodes))
        for node in found_nodes:
            self.assertEqual(source_node.value, node.value)

    def test_find_all_in_empty_list(self):
        node = Node(99)
        found_nodes = self.list.find_all(node.value)

        self.assertEqual(0, self.list.len())
        self.assertEqual([], found_nodes)

    def test_len(self):
        nodes = self.populate_list(self.list)
        self.assertEqual(len(nodes), self.list.len())

    def test_clean(self):
        nodes = self.populate_list(self.list)
        self.list.clean()

        self.assertIsNone(self.list.head)
        self.assertIsNone(self.list.tail)
        for node in nodes:
            self.assertIsNone(node.next)

    def test_insert_after(self):
        node = Node(99)
        prev_node = Node(77)
        self.list.add_in_tail(Node(35))
        self.list.add_in_tail(prev_node)
        self.list.add_in_tail(Node(64))
        self.list.insert(prev_node, node)

        self.assertEqual(4, self.list.len())
        self.assertEqual(node, prev_node.next)

    def test_insert_in_head(self):
        node = Node(99)
        nodes = self.populate_list(self.list)
        self.list.insert(None, node)

        self.assertEqual(node, self.list.head)
        self.assertNotEqual(node, self.list.tail)
        self.assertEqual(nodes[len(nodes) - 1], self.list.tail)
        self.assertEqual(len(nodes) + 1, self.list.len())

    def test_insert_multiple(self):
        prev_node = None
        nodes = (Node(12), Node(34), Node(56),)
        for node in nodes:
            self.list.insert(prev_node, node)
            prev_node = node

        self.assertEqual(len(nodes), self.list.len())
        self.assertEqual(nodes[0], self.list.head)
        self.assertEqual(nodes[len(nodes) - 1], self.list.tail)

    def test_insert_in_tail(self):
        node = Node(99)
        nodes = self.populate_list(self.list)
        self.list.insert(self.list.tail, node)

        self.assertNotEqual(node, self.list.head)
        self.assertEqual(nodes[0], self.list.head)
        self.assertEqual(node, self.list.tail)
        self.assertEqual(len(nodes) + 1, self.list.len())

    def test_insert_in_empty_list(self):
        node = Node(99)
        self.list.insert(None, node)

        self.assertEqual(node, self.list.head)
        self.assertEqual(node, self.list.tail)
        self.assertEqual(1, self.list.len())

    def test_delete_in_head(self):
        node = Node(99)
        node_alt = Node(node.value)
        self.list.add_in_tail(node)
        nodes = self.populate_list(self.list)
        self.list.add_in_tail(node_alt)
        self.list.delete(node.value)

        self.assertEqual(len(nodes) + 1, self.list.len())
        self.assertEqual(1, len(self.list.find_all(node.value)))
        self.assertNotEqual(node, self.list.head)
        self.assertEqual(nodes[0], self.list.head)
        self.assertEqual(node_alt, self.list.tail)
        self.assertIsNone(node.next)

    def test_delete_in_tail(self):
        node = Node(99)
        nodes = self.populate_list(self.list)
        self.list.add_in_tail(node)
        self.list.delete(node.value)

        self.assertEqual(len(nodes), self.list.len())
        self.assertEqual(0, len(self.list.find_all(node.value)))
        self.assertEqual(nodes[0], self.list.head)
        self.assertNotEqual(node, self.list.tail)
        self.assertEqual(nodes[len(nodes) - 1], self.list.tail)
        self.assertIsNone(node.next)

    def test_delete_all(self):
        node = Node(99)
        node_alt = Node(node.value)
        self.list.add_in_tail(node)
        nodes = self.populate_list(self.list)
        self.list.add_in_tail(node_alt)
        self.list.delete(node.value, True)

        self.assertEqual(len(nodes), self.list.len())
        self.assertEqual(0, len(self.list.find_all(node.value)))
        self.assertNotEqual(node, self.list.head)
        self.assertEqual(nodes[0], self.list.head)
        self.assertNotEqual(node_alt, self.list.tail)
        self.assertEqual(nodes[len(nodes) - 1], self.list.tail)
        self.assertIsNone(node.next)
        self.assertIsNone(node_alt.next)

    def test_delete_all_with_sequentially_nodes(self):
        node = Node(99)
        node_alt = Node(node.value)
        node_result = Node(8)
        self.list.add_in_tail(node)
        self.list.add_in_tail(node_alt)
        self.list.add_in_tail(node_result)
        self.list.delete(node.value, True)

        self.assertEqual(1, self.list.len())
        self.assertEqual(0, len(self.list.find_all(node.value)))
        self.assertNotEqual(node, self.list.head)
        self.assertNotEqual(node_alt, self.list.head)
        self.assertEqual(node_result, self.list.head)
        self.assertNotEqual(node, self.list.tail)
        self.assertNotEqual(node_alt, self.list.tail)
        self.assertEqual(node_result, self.list.tail)
        self.assertIsNone(node.next)
        self.assertIsNone(node_alt.next)

    def test_delete_all_in_empty_list(self):
        self.list.delete(99, True)

        self.assertEqual(0, self.list.len())
        self.assertIsNone(self.list.head)
        self.assertIsNone(self.list.tail)

    def test_delete_all_in_one_elem_list(self):
        node = Node(99)
        self.list.add_in_tail(node)
        self.list.delete(node.value, True)

        self.assertEqual(0, self.list.len())
        self.assertIsNone(self.list.head)
        self.assertIsNone(self.list.tail)
        self.assertIsNone(node.next)

    @staticmethod
    def populate_list(llist: LinkedList):
        nodes = (Node(12), Node(34), Node(56),)
        for node in nodes:
            llist.add_in_tail(node)

        return nodes


if __name__ == '__main__':
    unittest.main()
