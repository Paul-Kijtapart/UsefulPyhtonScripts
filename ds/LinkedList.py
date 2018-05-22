class Node:

    def __init__(self, val):
        self.next = None
        self.val = val

    def __repr__(self):
        return self.val


class LinkedListException(Exception):

    def __init__(self, message, errors):
        # Call the base class constructor with the parameters it needs
        super(LinkedListException, self).__init__(message)

        # Now for your custom code...
        self.errors = errors


class EmptyLinkedListException(LinkedListException):
    def __init__(self, message, errors):
        # Call the base class constructor with the parameters it needs
        super(EmptyLinkedListException, self).__init__(message)

        # Now for your custom code...
        self.errors = errors


class LinkedList:

    def __init__(self):
        self.front = None
        self.last = None

    def size(self):
        """
        Return the count of nodes in this linked list

        Returns:
            int
        """

        res = 0

        runner = self.front

        while runner is not None:
            res += 1
            runner = runner.next

        return res

    def unshift(self, val):
        """
        Add a new node with the given val to the linked list

        Args:
            val:

        Returns:

        """

        new_node = Node(val)

        if self.is_empty():
            self.last = new_node
            self.front = new_node
        else:
            new_node.next = self.front
            self.front = new_node

    def add(self, val):
        """
        Added a new node with the given val to the END of this linked list

        Args:
            val:

        Returns:
            Node - the newly added node with the given val
        """
        new_node = Node(val)

        if self.is_empty():
            self.front = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        return new_node

    def is_empty(self):
        """
        Return True if this linked list has no node. Otherwise, return False

        Returns:
            bool
        """
        return self.front is None

    def remove(self, val):
        """
        Remove the given val from this linked list

        Args:
            val:

        Returns:

        """
        if self.is_empty():
            raise EmptyLinkedListException()

        # check front
        while self.front.val == val:
            self.front = self.front.next

        # check middle
        runner = self.front
        prev = None

        while runner.next is not None:
            # if found matched
            if runner.val == val:
                prev.next = runner.next

            # if not matched
            else:
                prev = runner

            runner = runner.next

        # check last node
        if runner.val == val:
            # perform remove
            prev.next = runner.next

            # update last pointer
            self.last = prev

    def __str__(self):
        res = ""

        runner = self.front

        while runner is not None:
            res += runner.val + '->'
            runner = runner.next

        return res

    def get(self, val):
        """
        Return the first node with the given val. Otherwise, return None

        Args:
            val:

        Returns:
            Node

        """
        if self.is_empty():
            raise EmptyLinkedListException()

        runner = self.front

        while runner is not None:

            if runner.val == val:
                return runner

            runner = runner.next

        return None

    def first(self):
        """
        Return the first node of this linked list.

        Returns:
            Node - first node in this linked list

        Throws:
            EmptyLinkedListException - if this linked list is empty
        """
        if self.is_empty():
            raise EmptyLinkedListException()

        return self.front

    def end(self):
        if self.is_empty():
            raise EmptyLinkedListException

        return self.last
