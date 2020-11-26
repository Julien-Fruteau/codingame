from typing import Iterable, Iterator, Literal, Optional


class Vertex(int):
    discovered: bool = False

    def __new__(cls, value: int):
        this = int.__new__(cls, value)
        return this


class Edge:
    # definition for undirected graph
    def __init__(self, n1: Vertex, n2: Vertex):
        self.a: Vertex
        self.b: Vertex
        if n1 <= n2:
            self.a = n1
            self.b = n2
        else:
            self.a = n2
            self.b = n1


class Graph:
    def __init__(self, edges: Iterable[Edge]=None):
        self.E: list[Edge] = [] if edges is None else list(set(edges))
        self.V: list[Vertex] = self.getVertices()

    def getVertices(self) -> list[Vertex]:
        # return []
        return [e.a for e in self.E]

    def __add__(self, other: Edge):
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

