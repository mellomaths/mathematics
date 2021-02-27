class Graph:

    def __init__(self, number_of_vertices: int, edges: list) -> None:
        self.edges = edges
        self.number_of_vertices = number_of_vertices
        self.number_of_edges = len(edges)
        self.representation = Representation(number_of_vertices, edges)


class Representation:

    def __init__(self, number_of_vertices: int, edges: list) -> None:
        self.edges = edges
        self.number_of_vertices = number_of_vertices
        self.number_of_edges = len(edges)

    def incidence_matrix(self):
        n = self.number_of_vertices
        ind_matrix = [[0 for i in range(n)] for i in range(n)]
        for edge in self.edges:
            ind_matrix[edge[0] - 1][edge[1] - 1] = 1
            ind_matrix[edge[1] - 1][edge[0] - 1] = 1
        return ind_matrix

    def adjacency_list(self):
        n = self.number_of_vertices
        adj_list = [[] for i in range(n)]
        for edge in self.edges:
            adj_list[edge[0] - 1].append(edge[1] - 1)
            adj_list[edge[1] - 1].append(edge[0] - 1)
        return adj_list


# n = 8
# edges = [
#     (1, 2),
#     (1, 4),
#     (1, 5),
#     (2, 3),
#     (2, 6),
#     (3, 4),
#     (3, 7),
#     (4, 8),
#     (5, 6),
#     (5, 7),
#     (6, 8),
#     (7, 8)
# ]
# graph = Graph(n, edges)
