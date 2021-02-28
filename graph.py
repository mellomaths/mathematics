class Graph:

    def __init__(self, number_of_vertices: int, edges: list) -> None:
        self.edges = edges
        self.number_of_vertices = number_of_vertices
        self.number_of_edges = len(edges)
        self.representation = Representation(number_of_vertices, edges)

    def degrees(self) -> list:
        d = [0 for i in range(self.number_of_vertices)]
        adjacency_list = self.representation.adjacency_list()
        for i, node_adj_list in enumerate(adjacency_list):
            d[i] = len(node_adj_list)

        return d

    def node_degree(self, node_id: int) -> int:
        node_id = node_id - 1
        degrees = self.degrees()
        node_degree = degrees[node_id]
        return node_degree


class Representation:

    def __init__(self, number_of_vertices: int, edges: list) -> None:
        self.edges = edges
        self.number_of_vertices = number_of_vertices
        self.number_of_edges = len(edges)

    def adjacency_matrix(self) -> list:
        n = self.number_of_vertices
        adj_matrix = [[0 for i in range(n)] for i in range(n)]
        for edge in self.edges:
            adj_matrix[edge[0] - 1][edge[1] - 1] = 1
            adj_matrix[edge[1] - 1][edge[0] - 1] = 1
        return adj_matrix

    def adjacency_list(self) -> list:
        n = self.number_of_vertices
        adj_list = [[] for i in range(n)]
        for edge in self.edges:
            adj_list[edge[0] - 1].append(edge[1] - 1)
            adj_list[edge[1] - 1].append(edge[0] - 1)
        return adj_list
    
    def directed_adjacency_list(self) -> list:
        n = self.number_of_vertices
        adj_list = [[] for i in range(n)]
        for edge in self.edges:
            adj_list[edge[0] - 1].append(edge[1] - 1)
        return adj_list
