from unittest import TestCase

from ds.Graph import Graph


class TestGraph(TestCase):

    def setUp(self):
        vals = ['a', 'b', 'c', 'd', 'e', 'f']
        edges = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]

        # initialize graph
        self.graph = Graph()

        # add nodes
        for val in vals:
            self.graph.add_val(val)

        # add edges between nodes
        for edge in edges:
            self.graph.add_edge(edge[0], edge[1])

        # given
        vals2 = ['s', 'a', 'b', 'f']
        edges2 = [('s', 'a', 2), ('s', 'b', 6), ('a', 'b', 3), ('b', 'f', 1), ('a', 'f', 5)]

        self.graph2 = Graph()

        # add nodes
        for val in vals2:
            self.graph2.add_val(val)

        # add edges between nodes
        for edge in edges2:
            self.graph2.add_edge(edge[0], edge[1], edge[2])

    def test_get_topological_order(self):

        # Given
        graph = self.graph
        self.assertEqual(graph.node_count(), 6)

        # then
        self.assertIsNotNone(graph.get_topological_order())

    def test_has_path(self):

        # Given
        graph = self.graph

        # transitivity
        node_a = graph.get_or_create('a')
        node_c = graph.get_or_create('c')

        self.assertTrue(graph.has_path(node_a, node_c))

        node_e = graph.get_or_create('e')
        self.assertFalse(graph.has_path(node_a, node_e))

    def test_get_cheapest_path(self):
        graph = self.graph2

        # then
        from_node = graph.get_or_create('s')
        to_node = graph.get_or_create('f')

        cheapest_path = graph.get_cheapest_path(from_node, to_node)

        print(cheapest_path)

        self.assertIsNotNone(cheapest_path)

    def test_get_nodes_between(self):
        graph = self.graph2

        # then
        from_node = graph.get_or_create('s')
        to_node = graph.get_or_create('f')

        nodes = graph.get_nodes_between(from_node, to_node)

        self.assertEqual(len(nodes), 2)