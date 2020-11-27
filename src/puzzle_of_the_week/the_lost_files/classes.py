from typing import Iterable, Iterator, Literal, Optional, Sequence


class Vertex(int):
    discovered: bool = False

    def __new__(cls, value: int):
        this = int.__new__(cls, value)
        return this


class Edge(list):
    # definition for undirected graph
    def __init__(self, v1: Vertex, v2: Vertex):
        self.vertices = sorted([v1, v2])

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


class Tile:
    """Composed of a set of Vertices and a set Edges
    """

    def __init__(self):
        self.vertices: set[Vertex]
        self.edges: set[Edge]

    def add(self, v: Vertex) -> None:
        pass
        # self.vertices.append(v)


class Continent:
    def __init__(self, tile: Tile=None) -> None:
        self.tile: list[Tile] = [tile] if tile else []


class Graph:
    def __init__(self, edges: Iterable[Edge]=None):
        self.E: list[Edge] = list(edges) if edges else []

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


# class EdgeManager:
#     def __init__(self):
#         self.edges: list[Edge] = []

#     def add(self, edge: Edge) -> None:
#         self.edges.append(edge)
