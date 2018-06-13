from unittest import TestCase

from ds.Graph import Graph


class TestGraph(TestCase):
    def test_get_topological_order(self):
        vals = ['a', 'b', 'c', 'd', 'e', 'f']
        edges = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]

        # initailize graph
        graph = Graph()

        # add nodes
        for val in vals:
            graph.add_val(val)

        self.assertEqual(graph.node_count(), 6)

        # add edges between nodes
        for edge in edges:
            graph.add_edge(edge[0], edge[1])

        topological_order = graph.get_topological_order()
        self.assertIsNotNone(topological_order)
