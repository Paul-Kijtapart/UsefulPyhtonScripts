from unittest import TestCase

from ds.BST import BST


class TestBST(TestCase):

    def setUp(self):
        self.empty_tree = BST()

    def test_add(self):
        # Given
        before_node_count = self.empty_tree.size()

        # When
        self.empty_tree.add(2)
        self.empty_tree.add(3)
        self.empty_tree.add(1)

        # then

        # Order need to be in in-order
        self.assertEqual(self.empty_tree.to_array(), [1, 2, 3])

        # Size of the tree should be updated
        self.assertEqual(self.empty_tree.size(), before_node_count + 3)

    def test_remove(self):
        self.fail()

    def test_get(self):
        # When
        self.empty_tree.add(2)
        self.empty_tree.add(3)
        self.empty_tree.add(1)

        # then

        # there should exists a node for each added val
        self.assertIsNotNone(self.empty_tree.get(2))
        self.assertIsNotNone(self.empty_tree.get(3))
        self.assertIsNotNone(self.empty_tree.get(1))

        # get value not in the tree should return None
        self.assertIsNone(self.empty_tree.get(5))

    def test_is_empty(self):
        self.fail()

    def test_size(self):
        self.fail()

    def test_count_node(self):
        self.fail()

    def test_add_helper(self):
        self.fail()
