from typing import Iterable, Iterator, Optional


class Vertex(int):
    def __init__(self, value):
        super().__init__()
        self.discovered = False


class Edge:
    # definition for undirected graph
    def __init__(self, n1: int, n2: int):
        if n1 <= n2:
            self.a = n1
            self.b = n2
        else:
            self.a = n2
            self.b = n1


# class EdgeSet(set):
#     def __init__(self, edges: Iterable[Edge]=None) -> None:
#         self.E: set[Edge] = set() if edges is None else set(edges)

#     def __contains__(self, item: Edge) -> bool:
#         return item in self.E

#     def __len__(self) -> int:
#         return len(self.E)

#     def __iter__(self) -> Iterator[Edge]:
#         return iter(self.E)

#     def __getitem__(self, index: int) -> Edge:
#         return list(self.E)[index]


class Graph:
    def __init__(self, edges: Iterable[Edge]=None):
        self.E: list[Edge] = [] if edges is None else list(set(edges))
        self.V: list[int] = []

    def __add__(self, other: Edge):
        self.E.append(other)
        return Graph(self.E)

    def __iadd__(self, other: Edge):
        if other not in self.E:
            self.E.append(other)
        return self


class EdgeManager:
    def __init__(self):
        self.edges: list[Edge] = []

    def add(self, edge: Edge) -> None:
        self.edges.append(edge)


class Tile:
    """Composed of a set of Vertices and a set Edges
    """
    def __init__(self):
        self.vertices: set[Vertex]
        self.edges: set[Edge]

    def add(self, v: Vertex) -> None:
        pass
        # self.vertices.append(v)


class TileManager:
    def __init__(self) -> None:
        self.tiles: list[Tile] = []
    # if total tile = 0
    #  create a new tile
    #  add the edge
    # else
    #  for vertex in edge
    #   if vertex


class Continent:
    def __init__(self, tile: Tile) -> None:
        self.tile: list[Tile] = []
        self.tile.append(tile)


class ContinentManager:
    pass
    # while Tile
        # if len(continent) = 0
        #   create Continent(current_tile)
        # else
        # for continent in continents
        #   if a tile as an edge in common with all current continent tile
        #     add tile to continent
        #   else
        #     continue
        # if tile not added
        #   create Continent(current_tile)

