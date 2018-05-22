from unittest import TestCase

from ds.LinkedList import LinkedList, EmptyLinkedListException, LinkedListException


class TestLinkedList(TestCase):

    def setUp(self):
        self.empty_linked_list = LinkedList()

        self.letter_linked_list = LinkedList()
        self.letter_linked_list.unshift('a')
        self.letter_linked_list.unshift('b')
        self.letter_linked_list.unshift('c')

    def test_unshift(self):
        # before actions
        current_size = self.letter_linked_list.size()

        # given added new val to the front
        self.letter_linked_list.unshift('d')

        # size of linked list should change if we add new nodes to it
        self.assertEqual(self.letter_linked_list.size(), current_size + 1)

        # the new val should appear at the front of the linked list
        self.assertEqual(self.letter_linked_list.first().val, 'd')

    def test_add(self):
        # before actions
        current_size = self.letter_linked_list.size()

        # given added new val to the front
        self.letter_linked_list.add('d')

        # size of linked list should change if we add new nodes to it
        self.assertEqual(self.letter_linked_list.size(), current_size + 1)

        # the new val should appear at the front of the linked list
        self.assertEqual(self.letter_linked_list.end().val, 'd')

    def test_is_empty(self):
        # newly created linkedlist should be empty
        self.assertTrue(self.empty_linked_list)

        # should return False if linked list has some nodes
        self.assertFalse(self.letter_linked_list.is_empty())

    def test_remove(self):
        # size of linked list should change if we remove existing nodes
        current_size = self.letter_linked_list.size()
        self.letter_linked_list.remove('a')
        self.assertEqual(self.letter_linked_list.size(), current_size - 1)

    def test_get(self):
        # should return the Node if given existing val
        self.assertIsNotNone(self.letter_linked_list.get('a'))
