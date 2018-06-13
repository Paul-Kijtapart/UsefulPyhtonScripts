# libraries

class Node:
    # 3 Node status
    UNVISITED = 'UNVISITED'
    VISITED = 'VISITED'
    VISITING = 'VISITING'

    def __init__(self, val):
        self.val = val

        self.status = self.UNVISITED

        self.children = []
        self.childMap = dict()

        self.num_dependencies = 0

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)

    def add_child(self, child):
        # update state
        self.children.append(child)
        self.childMap[child.val] = child

        # update child
        child.increment_dependency()

    def increment_dependency(self):
        self.num_dependencies += 1

    def decrement_dependency(self):
        self.num_dependencies -= 1


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

    def node_count(self):
        """Return the total number of node"""
        return len(self.nodes)

    def add_edge(self, from_val, to_val):
        """
        Add edge from a node with from_val to a node with to_val
        if from_val/to_val does not exist, it will be created into a new node

        Args:
            from_val:
            to_val:

        Returns:
            None
        """

        from_node = self.get_or_create(from_val)
        to_node = self.get_or_create(to_val)

        # link them
        from_node.add_child(to_node)

    def get_or_create(self, val):
        """
        Get a node with the given val. Otherwise, create a new one with the val

        Args:
            val:

        Returns:
            Node : node with the given val
        """

        res = Node

        if self.has(val):
            res = self.nodeMap[val]
        else:
            res = self.add_val(val)

        return res

    def reset_status(self):
        """Reset the status of all nodes in thie graph"""

        for node in self.nodes:
            node.status = Node.UNVISITED

    def get_topological_order(self) -> list:

        self.reset_status()

        nodes = self.nodes

        ordered_nodes = []

        while True:

            all_checked = True

            # find node with 0 dep
            for node in nodes:

                # if found node with 0 dep
                if node.status == Node.UNVISITED and node.num_dependencies == 0:
                    # update dep of its children
                    for child in node.children:
                        child.decrement_dependency()

                    # add to the order list
                    ordered_nodes.append(node)

                    # mark that node as visited
                    node.status = Node.VISITED

                    # no cycle for this round
                    all_checked = False

            if all_checked:
                break

        return ordered_nodes

    def has(self, val):
        """
        Check if there exists a node with the given val

        Args:
            val:

        Returns:
            bool: True if there exists a node with the given val. Otherwise, False
        """
        return val in self.nodeMap

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
