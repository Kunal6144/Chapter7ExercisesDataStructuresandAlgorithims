class Vertex:
    def __init__(self, label):
        self.label = label

class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

class Graph:
    def __init__(self, adjacency_map):
        self.adjacency_map = adjacency_map

def DFS(graph, vertex, visited=None):
    if visited is None:
        visited = {}
    if vertex not in visited:
        visited[vertex] = None
        neighbors = graph.adjacency_map.get(vertex, {})
        for neighbor in neighbors:
            DFS(graph, neighbor, visited)
    return visited

# Example usage
A = Vertex('A')
B = Vertex('B')
C = Vertex('C')
D = Vertex('D')
E = Vertex('E')
F = Vertex('F')

AB = Edge(A, B, 2)
AC = Edge(A, C, 4)
BD = Edge(B, D, 5)
CD = Edge(C, D, 9)
CE = Edge(C, E, 3)
DF = Edge(D, F, 2)
EF = Edge(E, F, 2)

adj_map = {
    A: { B: AB, C: AC },
    B: { A: AB, D: BD },
    C: { A: AC, D: CD, E: CE },
    D: {B: BD, C: CD, F: DF},
    E: {C: CE, F: EF},
    F: {D: DF, E: EF}
}

g = Graph(adj_map)
print(DFS(g, A))
