from graph import Graph
import unittest
import random


class TestGraph(unittest.TestCase):


    def setUp(self) -> None:
        self.number_of_vertices = 8
        self.edges = [
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
        self.graph = Graph(self.number_of_vertices, self.edges)

    def tearDown(self) -> None:
        self.number_of_vertices = 0
        self.edges = []
        self.graph = None

    def generate_random_edges(self, n, m) -> list:
        edges = []
        for i in range(m):
            e = (random.randint(0, n), random.randint(0, n))
            edges.append(e)
        return edges

    def test_graph_init(self):
        graph = self.graph
        self.assertEqual(graph.number_of_edges, len(self.edges))

    def test_graph_degrees(self):
        graph = self.graph
        self.assertListEqual(graph.degrees(), [3, 3, 3, 3, 3, 3, 3, 3])
        self.assertEqual(graph.node_degree(1), 3)


if __name__ == "__main__":
    unittest.main()
