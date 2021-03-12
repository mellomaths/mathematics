class Graph:

    """
    Vertex ID should be greater than 0, starting with 1 to the total number of vertices.

    Example:
        if number_of_vertices is equals to 3:
        the graph should have 3 vertices: 1, 2 and 3.
    """

    def __init__(self, number_of_vertices: int, edges: list) -> None:
        self.edges = edges
        self.number_of_vertices = number_of_vertices
        self.number_of_edges = len(edges)
        self.representation = Representation(number_of_vertices, edges)


    def degrees(self) -> list:
        degrees = [0 for i in range(self.number_of_vertices)]
        adjacency_list = self.representation.adjacency_list()
        for i, vertex_adj_list in enumerate(adjacency_list):
            degrees[i] = len(vertex_adj_list)

        return degrees

    def vertex_degree(self, vertex_id: int) -> int:
        vertex_id = vertex_id - 1
        degrees = self.degrees()
        vertex_degree = degrees[vertex_id]
        return vertex_degree

    def fathers(self) -> list:
        # Every vertex is itself's father
        fathers = [i for i in range(self.number_of_vertices)]

        for edge in self.edges:
            fathers = UnionFind.union(fathers, edge[0] - 1, edge[1] - 1)

        return fathers

    def is_connected(self) -> bool:
        fathers = self.fathers()
        
        components = 0
        for i in range(len(fathers)):
            if fathers[i] == i:
                components += 1
        
        return components == 1

    def bridges(self) -> list:
        n = self.number_of_vertices
        visit_order = [0 for i in range(n)]
        low = [0 for i in range(n)]
        adjacency_matrix = self.representation.adjacency_matrix()
        bridges = []
        order = 0
        for i in range(n):
            if visit_order[i] == 0:
                bridges = Search.bridges(bridges, order, visit_order, low, adjacency_matrix, n, i, i)
        return bridges


class Search:

    @staticmethod
    def bridges(bridges: list, order: int, visit_order: list, low: list, adjacency_matrix: list, number_of_vertices: int, father: int, child: int):
        order += 1
        visit_order[child] = order
        for i in range(number_of_vertices):
            if adjacency_matrix[child][i] == 1: # has an edge between "child" and "i"
                if visit_order[i] == 0: # not visited
                    bridges = Search.bridges(bridges, order, visit_order, low, adjacency_matrix, number_of_vertices, child, i)
                    if low[i] == visit_order[i]:
                        bridges.append((child, i))
                        # thats a bridge
                    low[child] = min(low[child], low[i])
                elif i != father: # is not the current father
                    # updates the lowest
                    low[child] = min(low[child], visit_order[i])
        return bridges


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
