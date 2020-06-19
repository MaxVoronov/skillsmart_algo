import unittest
from src.ordered_list import OrderedList, OrderedStringList, Node


class TestOrderedList(unittest.TestCase):
    def test_compare_integer(self):
        lst = OrderedList(True)
        self.assertEqual(-1, lst.compare(2, 3))
        self.assertEqual(0, lst.compare(2, 2))
        self.assertEqual(1, lst.compare(3, 2))

    def test_compare_string(self):
        lst = OrderedStringList(True)
        self.assertEqual(-1, lst.compare("abc", "bcd"))
        self.assertEqual(-1, lst.compare("  abc ", " bcd  "))
        self.assertEqual(0, lst.compare("abc", "abc"))
        self.assertEqual(0, lst.compare("  abc ", " abc  "))
        self.assertEqual(1, lst.compare("bcd", "abc"))
        self.assertEqual(1, lst.compare("  bcd ", " abc  "))

    def test_add_asc_integer(self):
        lst = OrderedList(True)
        nodes = (Node(1), Node(2), Node(3), Node(4),)
        lst.add(nodes[1].value)
        lst.add(nodes[3].value)
        lst.add(nodes[0].value)
        lst.add(nodes[2].value)

        self.assertEqual(len(nodes), lst.len())
        self.assertEqual(nodes[0].value, lst.head.value)
        self.assertIsNotNone(lst.head.next)
        self.assertEqual(nodes[1].value, lst.head.next.value)
        self.assertEqual(nodes[len(nodes) - 1].value, lst.tail.value)
        self.assertEqual(nodes[len(nodes) - 2].value, lst.tail.prev.value)

    def test_add_desc_integer(self):
        lst = OrderedList(False)
        nodes = (Node(1), Node(2), Node(3), Node(4),)
        lst.add(nodes[1].value)
        lst.add(nodes[3].value)
        lst.add(nodes[0].value)
        lst.add(nodes[2].value)

        self.assertEqual(len(nodes), lst.len())
        self.assertEqual(nodes[len(nodes) - 1].value, lst.head.value)
        self.assertIsNotNone(lst.head.next)
        self.assertEqual(nodes[len(nodes) - 2].value, lst.head.next.value)
        self.assertEqual(nodes[0].value, lst.tail.value)
        self.assertEqual(nodes[1].value, lst.tail.prev.value)

    def test_add_asc_string(self):
        lst = OrderedStringList(True)
        nodes = (Node(" abc   "), Node("  bcd "), Node("cde  "), Node("def "),)
        lst.add(nodes[0].value)
        lst.add(nodes[3].value)
        lst.add(nodes[2].value)
        lst.add(nodes[1].value)

        self.assertEqual(len(nodes), lst.len())
        self.assertEqual(nodes[0].value, lst.head.value)
        self.assertIsNotNone(lst.head.next)
        self.assertEqual(nodes[1].value, lst.head.next.value)
        self.assertEqual(nodes[3].value, lst.tail.value)
        self.assertEqual(nodes[2].value, lst.tail.prev.value)

    def test_add_desc_string(self):
        lst = OrderedStringList(False)
        nodes = (Node("abc"), Node("bcd"), Node("cde"), Node("def"),)
        lst.add(nodes[3].value)
        lst.add(nodes[1].value)
        lst.add(nodes[0].value)
        lst.add(nodes[2].value)

        self.assertEqual(len(nodes), lst.len())
        self.assertEqual(nodes[len(nodes) - 1].value, lst.head.value)
        self.assertIsNotNone(lst.head.next)
        self.assertEqual(nodes[len(nodes) - 2].value, lst.head.next.value)
        self.assertEqual(nodes[0].value, lst.tail.value)
        self.assertEqual(nodes[1].value, lst.tail.prev.value)

    def test_find_asc_integer(self):
        lst = OrderedList(True)
        nodes = self.populate_integer_list(lst)
        for node in nodes:
            found_node = lst.find(node.value)
            self.assertIsNotNone(found_node)
            self.assertEqual(node.value, found_node.value)
        self.assertIsNone(lst.find(999))

    def test_find_desc_integer(self):
        lst = OrderedList(False)
        nodes = self.populate_integer_list(lst)
        for node in nodes:
            found_node = lst.find(node.value)
            self.assertIsNotNone(found_node)
            self.assertEqual(node.value, found_node.value)
        self.assertIsNone(lst.find(999))

    def test_find_asc_strings(self):
        lst = OrderedStringList(True)
        nodes = self.populate_string_list(lst)
        for node in nodes:
            found_node = lst.find(node.value)
            self.assertIsNotNone(found_node)
            self.assertEqual(node.value, found_node.value)
        self.assertIsNone(lst.find("zzz"))

    def test_find_desc_strings(self):
        lst = OrderedStringList(False)
        nodes = self.populate_string_list(lst)
        for node in nodes:
            found_node = lst.find(node.value)
            self.assertIsNotNone(found_node)
            self.assertEqual(node.value, found_node.value)
        self.assertIsNone(lst.find("zzz"))

    def test_find_in_empty_list(self):
        lst = OrderedList(True)
        found_node = lst.find(123)
        self.assertEqual(0, lst.len())
        self.assertIsNone(lst.head)
        self.assertIsNone(lst.tail)
        self.assertIsNone(found_node)

    def test_delete_asc_integer(self):
        lst = OrderedList(True)
        nodes = self.populate_integer_list(lst)
        lst.delete(nodes[1].value)

        self.assertEqual(len(nodes) - 1, lst.len())
        for node in lst.get_all():
            self.assertNotEqual(nodes[1].value, node.value)

    def test_delete_desc_integer(self):
        lst = OrderedList(False)
        nodes = self.populate_integer_list(lst)
        lst.delete(nodes[1].value)

        self.assertEqual(len(nodes) - 1, lst.len())
        for node in lst.get_all():
            self.assertNotEqual(nodes[1].value, node.value)

    def test_delete_asc_string(self):
        lst = OrderedStringList(True)
        nodes = self.populate_string_list(lst)
        lst.delete(nodes[1].value)

        self.assertEqual(len(nodes) - 1, lst.len())
        for node in lst.get_all():
            self.assertNotEqual(nodes[1].value, node.value)

    def test_delete_in_empty_list(self):
        lst = OrderedList(True)
        lst.delete(123)
        self.assertEqual(0, lst.len())
        self.assertIsNone(lst.head)
        self.assertIsNone(lst.tail)

    def test_delete_in_one_elem_list(self):
        lst = OrderedList(True)
        lst.add(123)
        self.assertEqual(1, lst.len())
        lst.delete(123)
        self.assertEqual(0, lst.len())
        self.assertIsNone(lst.head)
        self.assertIsNone(lst.tail)

    def test_clean(self):
        lst = OrderedList(True)
        nodes = self.populate_integer_list(lst)
        lst.clean(True)

        self.assertEqual(0, lst.len())
        self.assertIsNone(lst.head)
        self.assertIsNone(lst.tail)
        for node in nodes:
            self.assertIsNone(node.prev)
            self.assertIsNone(node.next)

    def test_get_all_asc_integer(self):
        lst = OrderedList(True)
        nodes = self.populate_integer_list(lst)
        actual_nodes = lst.get_all()

        self.assertEqual(len(nodes), lst.len())
        self.assertEqual(len(actual_nodes), lst.len())
        for idx, node in enumerate(nodes, start=0):
            self.assertEqual(node.value, actual_nodes[idx].value)

    def test_get_all_desc_integer(self):
        lst = OrderedList(False)
        nodes = self.populate_integer_list(lst)
        actual_nodes = lst.get_all()

        self.assertEqual(len(nodes), lst.len())
        self.assertEqual(len(actual_nodes), lst.len())
        for idx, node in enumerate(reversed(nodes), start=0):
            self.assertEqual(node.value, actual_nodes[idx].value)

    def test_get_all_asc_string(self):
        lst = OrderedStringList(True)
        nodes = self.populate_string_list(lst)
        actual_nodes = lst.get_all()

        self.assertEqual(len(nodes), lst.len())
        self.assertEqual(len(actual_nodes), lst.len())
        for idx, node in enumerate(nodes, start=0):
            self.assertEqual(node.value, actual_nodes[idx].value)

    def test_get_all_desc_string(self):
        lst = OrderedStringList(False)
        nodes = self.populate_string_list(lst)
        actual_nodes = lst.get_all()

        self.assertEqual(len(nodes), lst.len())
        self.assertEqual(len(actual_nodes), lst.len())
        for idx, node in enumerate(reversed(nodes), start=0):
            self.assertEqual(node.value, actual_nodes[idx].value)

    @staticmethod
    def populate_integer_list(lst: OrderedList):
        nodes = (Node(123), Node(345), Node(567),)
        for node in nodes:
            lst.add(node.value)
        return nodes

    @staticmethod
    def populate_string_list(lst: OrderedList):
        nodes = (Node("abc "), Node("  bcd "), Node("  cde"),)
        for node in nodes:
            lst.add(node.value)
        return nodes


if __name__ == '__main__':
    unittest.main()
