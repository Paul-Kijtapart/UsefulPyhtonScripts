# libraries
from collections import deque, namedtuple
import math

# Edge model
Edge = namedtuple('Edge', ['node', 'cost'])


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

    def add_child(self, child, cost=0):
        # update state
        self.children.append(child)
        self.childMap[child.val] = Edge(node=child, cost=cost)

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

    def add_edge(self, from_val, to_val, cost=0):
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
        from_node.add_child(to_node, cost)

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

    def has_path(self, from_node: Node, to_node: Node) -> bool:
        """
        Check if there exists path between from_node and to_node

        Args:
            from_node(Node):
            to_node(Node):

        Returns:
            bool - True if there is a path. Otherwise, False
        """
        # reset status of the all nodes
        self.reset_status()

        # order of check matters
        queue = deque()

        if from_node.status == Node.UNVISITED:
            queue.append(from_node)

        while len(queue) > 0:

            # visit
            current_node = queue.popleft()

            # if found
            if current_node == to_node:
                return True

            # if Not found, keep on searching

            if current_node.status == Node.UNVISITED:

                # process the current node
                current_node.status = Node.VISITING

                # add child of the current node
                for child in current_node.children:

                    # add child that has not been processed
                    if child.status == Node.UNVISITED:
                        queue.append(child)

            # update status of the current node (Prevent-loop)
            current_node.status = Node.VISITED

        return False

    def get_shortest_path(self, from_node: Node, to_node: Node) -> list:
        """
        Return all nodes in the shortest path

        Args:
            from_node (Node):
            to_node (Node):

        Returns:
            list - of nodes to traverse from the from_node to to_node
        """
        pass

    def get_cheapest_path(self, from_node: Node, to_node: Node) -> list:
        """
        Return the cheapest path from the from_node to the to_node
        if there is NO path, return None

        Args:
            from_node(Node):
            to_node(Node):

        Returns:

        """

        if not self.has_path(from_node, to_node):
            return None

        self.reset_status()

        # identify all nodes between from_node and to_node
        nodes = self.get_nodes_between(from_node, to_node)

        # include to_node as well
        nodes.append(to_node)

        # keep track of min_cost to this node so far
        min_cost_dict = dict()

        # the best parent that give min_cost to this node
        parent_dict = dict()

        # initialize
        for node in nodes:
            min_cost_dict[node.val] = math.inf
            parent_dict[node.val] = None

        # apply children of the from_node to update state first
        for edge in from_node.childMap.values():
            min_cost_dict[edge.node.val] = edge.cost
            parent_dict[edge.node.val] = from_node

        to_be_processed = self._find_min_unvisited_node(nodes, min_cost_dict)
        while to_be_processed is not None:

            to_be_processed.status = Node.VISITING

            # update its children
            for edge in to_be_processed.childMap.values():
                current_cost = min_cost_dict[to_be_processed.val] + edge.cost

                if current_cost < min_cost_dict[edge.node.val]:
                    min_cost_dict[edge.node.val] = current_cost
                    parent_dict[edge.node.val] = to_be_processed

            # done with this node
            to_be_processed.status = Node.VISITED

            # find next min unvisited node
            to_be_processed = self._find_min_unvisited_node(nodes, min_cost_dict)

        # find path from the to_node
        cheapest_path = []

        current_parent = parent_dict[to_node.val]

        cheapest_path.append(current_parent)

        while current_parent != from_node:
            current_parent = parent_dict[current_parent.val]
            cheapest_path.append(current_parent)

        return cheapest_path

    def get_nodes_between(self, from_node: Node, to_node: Node) -> list:
        """
        Return list of nodes between from_node and to_node
        None if there is no path

        Args:
            from_node(Node):
            to_node(Node):

        Returns:
            list
        """

        all_paths = []

        self._get_nodes_between_helper(from_node, to_node, [], all_paths)

        nodes = set()
        for path in all_paths:
            for node in path:
                if node != to_node and node != from_node and node not in nodes:
                    nodes.add(node)

        return list(nodes)

    def _get_nodes_between_helper(self, root, to_node, current_path, all_paths):
        """DFS"""

        if root is None:
            return

        # visit

        # update current path
        current_path.append(root)

        # if we reach destination
        if root == to_node:
            all_paths.append(current_path.copy())

        # visit children
        for child in root.children:
            self._get_nodes_between_helper(child, to_node, current_path, all_paths)

        # revert current_path
        current_path.pop()

    def _find_min_unvisited_node(self, nodes, min_cost_dict):
        """
        Find node with min cost and status UNVISITED

        Args:
            nodes:

        Returns:
            Node | None
        """

        min_node = None
        min_cost = math.inf

        for node in nodes:
            if node.status == Node.UNVISITED and min_cost_dict[node.val] < min_cost:
                min_node = node
                min_cost = min_cost_dict[node.val]

        return min_node

    def has(self, val) -> bool:
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
