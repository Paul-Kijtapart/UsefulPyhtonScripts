class Node:

    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def __repr__(self):
        return str(self.val)

    def __str__(self):
        return str(self.val)


class BST:

    def __init__(self):
        self.root = None

    def add(self, val) -> Node:
        self.root = self._add_helper(val, self.root)

    def remove(self, val) -> Node:
        """Remove node with given val"""
        pass

    def get(self, val) -> Node:
        """
        Return node with the given val

        Args:
            val:

        Returns:
            Node|None: return the node with the given val in this tree. Otherwise, return None
        """

        return self._get_helper(self.root, val)

    def get_depth(self):
        """
        Return the Depth of this tree

        Returns:
            int: the depth of this tree
        """
        return self._get_depth_helper(self.root)

    def _get_depth_helper(self, root: Node) -> int:
        """
        Return the depth of the given tree

        Args:
            root(Node): root of the given tree

        Returns:
            int
        """
        if root is None:
            return 0

        left_depth = self._get_depth_helper(root.left)
        right_depth = self._get_depth_helper(root.right)

        return max(left_depth, right_depth) + 1

    def _get_helper(self, root: Node, val):
        """Search for the given val from the given tree"""

        if root is None:
            return None

        if root.val == val:
            return root

        elif root.val < val:
            # go right
            return self._get_helper(root.right, val)

        else:
            # go left
            return self._get_helper(root.left, val)

    def is_empty(self):
        """Check if this BST is empty"""
        return self.root is None

    def size(self):
        """Return the size of this BST"""
        return self.count_node(self.root)

    def to_array(self):
        """
        Return a array representation of this BST

        Returns:
            list: list of node values in BST order
        """

        res = []

        self._to_array_helper(self.root, res)

        return res

    @classmethod
    def count_node(cls, root: Node) -> int:
        """
        Return the number of nodes in the given tree

        Args:
            root(Node):

        Returns:
            int: number of nodes in the given tree
        """
        if root is None:
            return 0

        left_count = cls.count_node(root.left)
        right_count = cls.count_node(root.right)

        return left_count + right_count + 1

    def _add_helper(self, val, root) -> Node:
        """
        Add new node with given val to the tree
        and return root of the new tree

        Args:
            val: value to create an node with
            root(Node):

        Returns:
            Node: the updated root node of this tree
        """

        new_node = Node(val)

        if root is None:
            root = new_node
        elif root.val <= val:
            # add to the Right
            root.right = self._add_helper(val, root.right)
        else:
            # add to the Left
            root.left = self._add_helper(val, root.left)

        return root

    def _to_array_helper(self, root, array):
        """
        Traverse this tree in in-order order and update the array

        Args:
            root:
            array(list):

        Returns:

        """
        if root is None:
            return

        self._to_array_helper(root.left, array)
        array.append(root.val)
        self._to_array_helper(root.right, array)
