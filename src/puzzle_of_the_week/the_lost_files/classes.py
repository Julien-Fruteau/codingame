from typing import Iterable, Iterator, Literal, Optional, Sequence, Union


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

    def __iter__(self) -> Iterator[Vertex]:
        return iter(self.vertices)

    def __getitem__(self, s: slice) -> Sequence[Vertex]:
        return self.vertices[s]

    def __getitem__(self, s: int) -> Vertex:
        return self.vertices[s]

    def remove(self, value: Vertex) -> None:
        self.vertices.remove(value)

    def pop(self, index: int=-1) -> Vertex:
        return self.vertices[index]

    def Adj(self, v: Vertex) -> Union[Vertex, None]:
        if v not in self.vertices:
            return None
        return self.vertices[0] if v == self.vertices[1] else self.vertices[1]


# class Tile:
#     """Composed of a set of Vertices and a set Edges
#     """

#     def __init__(self):
#         self.vertices: set[Vertex]
#         self.edges: set[Edge]

#     def add(self, v: Vertex) -> None:
#         pass
#         # self.vertices.append(v)


# class Continent:
#     def __init__(self, vertices: Iterable[Vertex]) -> None:
#         self.vertices = list(vertices)


class Continent:
    def __init__(self, edges: Iterable[Edge]) -> None:
        self.E = list(edges)

    @property
    def V(self) -> list[Vertex]:
        res = []
        for e in self.E:
            res += [*e]
        return sorted(set(res))

    @property
    def totalTiles(self) -> int:
        return len(self.E) - len(self.V) + 1

class Graph:
    def __init__(self, edges: Iterable[Edge]=None):
        self.E: list[Edge] = list(edges) if edges else []
        self.C: list[Continent] = []
        # self.CE: list[ContinentE] = []

    @property
    def V(self) -> list[Vertex]:
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

    # def AdjV(self, v: Vertex) -> list[Vertex]:
    #     res: list[Vertex] = []
    #     for edge in self.E:
    #         adj = edge.Adj(v)
    #         if adj is not None:
    #             res.append(adj)
    #     return sorted(res)

    def AdjE(self, e: Edge) -> list[Edge]:
        res: list[Edge] = []
        for otherEdge in [edge for edge in self.E if edge is not e]:
            if e[0] in otherEdge or e[1] in otherEdge:
                res.append(otherEdge)
        return sorted(res)

    # def DFS(self, root: Vertex):
    #     root.discovered = True
    #     for v in self.AdjV(root):
    #         if not v.discovered:
    #             self.DFS(v)

    def DFS(self, root: Edge):
        root.discovered = True
        for e in self.AdjE(root):
            if not e.discovered:
                self.DFS(e)

    # def discoverContinents(self):
    #     for v in self.V:
    #         discovered = [v for v in self.V if v.discovered]
    #         if not v.discovered:
    #             self.DFS(v)
    #             disco = [v for v in self.V if v.discovered and v not in discovered]
    #             self.C.append(Continent(disco))

    def discoverContinents(self):
        for e in self.E:
            discovered = [e for e in self.E if e.discovered]
            if not e.discovered:
                self.DFS(e)
                disco = [e for e in self.E if e.discovered and e not in discovered]
                self.C.append(Continent(disco))

    # def getEdges(self, vertices: list[Vertex]) -> list[Edge]:
    #     res: list[Edge] = []
    #     return res
    
    # > init w/ 1st item...
    # root = self.V[0]
    # queue = [root]
    #
    # while len(queue) > 0:
    #   next = queue.pop()
    #   next.discovered = True
    #   for adj in self.Adj(nexr):
    #       if adj.discovered == False
    #           queue.append(adj)
    

