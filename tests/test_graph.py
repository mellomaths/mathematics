from graph import *
import unittest
import random


class TestGraph(unittest.TestCase):

    def mock_graph(self):
        n = 8
        edges = [
            (1, 2),
            (1, 4),
            (1, 5),
            (2, 3),
            (2, 6),
            (3, 4),
            (3, 7),
            (4, 8),
            (5, 6),
            (5, 7),
            (6, 8),
            (7, 8)
        ]
        return { "n": n, "edges": edges }

    def generate_random_edges(self, n, m):
        edges = []
        for i in range(m):
            e = (random.randint(0, n), random.randint(0, n))
            edges.append(e)
        return edges

    def test_graph_init(self):
        mock_graph = self.mock_graph()
        number_of_vertices = mock_graph["n"]
        edges = mock_graph["edges"]
        graph = Graph(number_of_vertices, edges)
        self.assertEqual(graph.number_of_vertices, number_of_vertices)
        self.assertEqual(graph.number_of_edges, len(edges))
        self.assertEqual(graph.edges, edges)


if __name__ == "__main__":
    unittest.main()
