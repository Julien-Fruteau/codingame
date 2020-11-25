import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

edgeMgr = EdgeManager()
tileMgr = TileManager()

e = int(input())
for i in range(e):
    n_1, n_2 = [int(j) for j in input().split()]
    edgeMgr.add(Edge((n_1, n_2)))
    
    if len(tiles) == 0:
        pass
    else:
        pass

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True


print("0 0")


# =======================


class Vertex:
    def __init__(self, vid):
        self.vid = vid


class Edge:
    def __init__(self, n: tuple):
        self.n_1 = n[0]
        self.n_2 = n[1]


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
        self.vertices.append(v)


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

