class Node:

    def __init__(self, val):
        self.val = val

        self.children = []
        self.childMap = dict()

    def __str__(self):
        return str(self.val)


class Graph:

    def __init__(self):
        self.nodes = []
        self.nodeMap = dict()

    def _add_node(self, node: Node) -> Node:
        """
        Add the given node to this graph

        Args:
            node (Node): the node to be added

        Returns:
            Node - the newly added node
        """

        self.nodes.append(node)
        self.nodeMap[node.val] = node

        return node

    def add_edge(self, from_val, to_val):
        """
        Add edge from a node with from_val to a node with to_val
        if from_val/to_val does not exist, it will be created into a new node

        Args:
            from_val:
            to_val:

        Returns:

        """

        pass

    def add_val(self, val) -> Node:
        """
        Add the given val as node in the graph

        Args:
            val:

        Returns:
            Node - the newly added node
        """
        return self._add_node(Node(val))

    def __str__(self):
        res = ""

        for node in self.nodes:
            res += node.__str__()

        return res
