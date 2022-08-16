import sys
import math

class Vertex(int):
    discovered: bool = False

    def __new__(cls, value: int):
        this = int.__new__(cls, value)
        return this


class Edge(list):
    # definition for undirected graph
    def __init__(self, v1: Vertex, v2: Vertex):
        self.vertices = sorted([v1, v2])
        self.discovered = False

    def __eq__(self, other) -> bool:
        return self is other

    def __contains__(self, v: Vertex) -> bool:
        return v in self.vertices

    def __len__(self) -> int:
        return len(self.vertices)

    def __iter__(self):
        return iter(self.vertices)

    def __getitem__(self, s: slice):
        return self.vertices[s]

    def __getitem__(self, s: int) -> Vertex:
        return self.vertices[s]

    def remove(self, value: Vertex) -> None:
        self.vertices.remove(value)

    def pop(self, index: int = -1) -> Vertex:
        return self.vertices[index]

    def Adj(self, v: Vertex):
        if v not in self.vertices:
            return None
        return self.vertices[0] if v == self.vertices[1] else self.vertices[1]


class Continent:
    def __init__(self, edges) -> None:
        self.E = list(edges)

    @property
    def V(self):
        res = []
        for e in self.E:
            res += [*e]
        return sorted(set(res))

    @property
    def totalTiles(self) -> int:
        return len(self.E) - len(self.V) + 1


class Graph:
    def __init__(self, edges=None):
        self.E = list(edges) if edges else []
        self.C = []
        # self.CE: list[ContinentE] = []

    @property
    def V(self):
        res = []
        for e in self.E:
            res += [*e]
        return sorted(set(res))

    def __add__(self, other: Edge):
        if other not in self.E:
            self.E.append(other)
        return Graph(self.E)

    def __iadd__(self, other: Edge):
        if other not in self.E:
            self.E.append(other)
        return self

    def AdjE(self, e: Edge):
        res = []
        for otherEdge in [edge for edge in self.E if edge is not e]:
            if e[0] in otherEdge or e[1] in otherEdge:
                res.append(otherEdge)
        return sorted(res)

    def DFS(self, root: Edge):
        root.discovered = True
        for e in self.AdjE(root):
            if not e.discovered:
                self.DFS(e)

    def discoverContinents(self):
        for e in self.E:
            discovered = [e for e in self.E if e.discovered]
            if not e.discovered:
                self.DFS(e)
                disco = [e for e in self.E if e.discovered and e not in discovered]
                self.C.append(Continent(disco))


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
G = Graph()
e = int(input())
for i in range(e):
    n_1, n_2 = [int(j) for j in input().split()]
    G += Edge(Vertex(n_1), Vertex(n_2))

G.discoverContinents()
C = len(G.C)
T = sum([c.totalTiles for c in G.C])
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(f"{C} {T}")
