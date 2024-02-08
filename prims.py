import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def prim_mst(self):
        mst = []
        visited = set()
        start_vertex = next(iter(self.graph))

        pq = [(0, start_vertex)]
        while pq:
            cost, u = heapq.heappop(pq)
            if u not in visited:
                visited.add(u)
                mst.append((u, cost))
                for v, w in self.graph[u]:
                    if v not in visited:
                        heapq.heappush(pq, (w, v))

        return mst

    def print_mst(self, mst):
        print("Minimum Spanning Tree:")
        for u, cost in mst:
            print(f"Edge: {u} -- cost: {cost}")


g = Graph()
g.add_edge('A', 'B', 6)
g.add_edge('A', 'C', 7)
g.add_edge('B', 'C', 8)
g.add_edge('B', 'D', 5)
g.add_edge('C', 'D', 3)
g.add_edge('C', 'E', 9)
g.add_edge('D', 'E', 7)

mst = g.prim_mst()
g.print_mst(mst)
