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
