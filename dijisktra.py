import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, w))

    def dijkstra(self, src):
        dist = {vertex: float('inf') for vertex in self.graph}
        dist[src] = 0
        pq = [(0, src)]

        while pq:
            curr_dist, u = heapq.heappop(pq)
            if curr_dist > dist[u]:
                continue

            for v, w in self.graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))

        self.print_solution(dist)

    def print_solution(self, dist):
        print("Vertex Distance from Source")
        for vertex, distance in dist.items():
            print(f"{vertex}\t\t{distance}")


g = Graph()
g.add_edge('A', 'B', 6)
g.add_edge('A', 'C', 7)
g.add_edge('B', 'C', 8)
g.add_edge('B', 'D', 5)
g.add_edge('C', 'D', -3)
g.add_edge('C', 'E', 9)
g.add_edge('D', 'E', 7)

g.dijkstra('A')
