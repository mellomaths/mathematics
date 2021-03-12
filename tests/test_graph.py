from logging import getLogRecordFactory
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
        self.assertEqual(graph.vertex_degree(1), 3)

    def test_graph_representation_adjacency_matrix(self):
        graph = self.graph
        matrix = [
            [0, 1, 0, 1, 1, 0, 0, 0],
            [1, 0, 1, 0, 0, 1, 0, 0],
            [0, 1, 0, 1, 0, 0, 1, 0],
            [1, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 1, 0],
            [0, 1, 0, 0, 1, 0, 0, 1], 
            [0, 0, 1, 0, 1, 0, 0, 1], 
            [0, 0, 0, 1, 0, 1, 1, 0]
        ]
        self.assertEqual(len(graph.representation.adjacency_matrix()), 8)
        self.assertTrue(len(graph.representation.adjacency_matrix()[0]), 8)
        self.assertTrue(len(graph.representation.adjacency_matrix()[1]), 8)
        self.assertTrue(len(graph.representation.adjacency_matrix()[2]), 8)
        self.assertTrue(len(graph.representation.adjacency_matrix()[3]), 8)
        self.assertTrue(len(graph.representation.adjacency_matrix()[4]), 8)
        self.assertTrue(len(graph.representation.adjacency_matrix()[5]), 8)
        self.assertTrue(len(graph.representation.adjacency_matrix()[6]), 8)
        self.assertTrue(len(graph.representation.adjacency_matrix()[7]), 8)
        self.assertEqual(graph.representation.adjacency_matrix(), matrix)
    
    def test_graph_representation_adjacency_list(self):
        graph = self.graph
        adj_list = [
            [1, 3, 4], 
            [0, 2, 5], 
            [1, 3, 6], 
            [0, 2, 7], 
            [0, 5, 6], 
            [1, 4, 7], 
            [2, 4, 7], 
            [3, 5, 6]
        ]
        self.assertListEqual(graph.representation.adjacency_list(), adj_list)
        total_length_adj_list = sum([len(element_adj_list) for element_adj_list in adj_list])

        # Rule: if the graph is not directed, 
        #  the sum of lengths of all adjacency lists should be equal to twice total of edges
        #  because an edge (u, v) appears twice meaning that the edge (v, u) also exists
        self.assertEqual(2 * graph.number_of_edges, total_length_adj_list)

    def test_graph_representation_directed_adjacency_list(self):
        graph = self.graph
        directed_adj_list = [
            [1, 3, 4], 
            [2, 5],
            [3, 6],
            [7],
            [5, 6],
            [7],
            [7],
            []
        ]
        self.assertListEqual(graph.representation.directed_adjacency_list(), directed_adj_list)
        total_length_adj_list = sum([len(element_adj_list) for element_adj_list in directed_adj_list])
        self.assertEqual(graph.number_of_edges, total_length_adj_list)

    def test_graph_is_connected(self):
        graph = self.graph
        self.assertTrue(graph.is_connected())

    def test_graph_fathers(self):
        graph = self.graph
        self.assertListEqual(graph.fathers(), [0, 0, 0, 0, 0, 0, 0, 0])

    def test_graph_bridges(self):
        number_of_vertices = 10
        edges = [
            (1, 2),
            (1, 3),
            (1, 4),
            (1, 8),
            (2, 5),
            (2, 3),
            (2, 7),
            (3, 5),
            (5, 6),
            (4, 8),
            (8, 9),
            (8, 10)
        ]
        graph = Graph(number_of_vertices, edges)
        print(graph.bridges())


if __name__ == "__main__":
    unittest.main()
