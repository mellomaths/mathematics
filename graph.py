class Graph:

    def __init__(self, number_of_vertices: int, edges: list) -> None:
        self.edges = edges
        self.number_of_vertices = number_of_vertices
        self.number_of_edges = len(edges)
        self.representation = Representation(number_of_vertices, edges)

    def degrees(self) -> list:
        d = [0 for i in range(self.number_of_vertices)]
        adjacency_list = self.representation.adjacency_list()
        for i, vertex_adj_list in enumerate(adjacency_list):
            d[i] = len(vertex_adj_list)

        return d

    def vertex_degree(self, vertex_id: int) -> int:
        vertex_id = vertex_id - 1
        degrees = self.degrees()
        vertex_degree = degrees[vertex_id]
        return vertex_degree

    def is_connected(self) -> bool:
        fathers = [0 for i in range(self.number_of_vertices)]

        for edge in self.edges:
            fathers = UnionFind.union(fathers, edge[0] - 1, edge[1] - 1)
        
        components = 0
        for i in range(len(fathers)):
            if fathers[i] == i:
                components += 1
        
        return components == 1


class UnionFind:

    @staticmethod
    def find(fathers: list, p: int) -> int:
        if fathers[p] != p:
            fathers[p] = UnionFind.find(fathers, fathers[p])
        return fathers[p]

    @staticmethod
    def union(fathers: list, p: int, q: int) -> list:
        p_father = UnionFind.find(fathers, p)
        q_father = UnionFind.find(fathers, q)
        if p_father < q_father:
            fathers[q_father] = p_father
        else:
            fathers[p_father] = q_father
        
        return fathers


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
