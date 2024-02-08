class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.vertex_dict = {}
        self.graph = []

        # Assigning an index to each vertex
        for i, vertex in enumerate(vertices):
            self.vertex_dict[vertex] = i

    def add_edge(self, u, v, w):
        u_index = self.vertex_dict[u]
        v_index = self.vertex_dict[v]
        self.graph.append([u_index, v_index, w])

    def bellman_ford(self, src):
        dist = [float("Inf")] * len(self.vertex_dict)
        src_index = self.vertex_dict[src]
        dist[src_index] = 0

        for _ in range(len(self.vertex_dict) - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        self.print_solution(dist)

    def print_solution(self, dist):
        print("Vertex Distance from Source")
        for vertex, index in self.vertex_dict.items():
            print(f"{vertex}\t\t{dist[index]}")


g = Graph(['A', 'B', 'C', 'D', 'E'])
g.add_edge('A', 'B', 6)
g.add_edge('A', 'C', 7)
g.add_edge('B', 'C', 8)
g.add_edge('B', 'D', 5)
g.add_edge('C', 'D', -3)
g.add_edge('C', 'E', 9)
g.add_edge('D', 'E', 7)

g.bellman_ford('A')
