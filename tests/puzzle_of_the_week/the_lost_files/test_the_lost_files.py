import pytest
from src.puzzle_of_the_week.the_lost_files.classes import Graph, Vertex, Edge


def test_Vertex():
    v = Vertex(1)
    w = Vertex(2)
    w.discovered = True
    assert v == 1 and v.discovered == False
    assert w == 2 and w.discovered == True

def test_Edge():
    e1 = Edge(Vertex(1), Vertex(2))
    e2 = Edge(Vertex(2), Vertex(2))
    e3 = Edge(Vertex(3), Vertex(2))
    assert e1[0] == 1 and e1[1] == 2
    assert e2[0] == 2 and e2[1] == 2
    assert e3[0] == 2 and e3[1] == 3

def test_Edge_getAdj():
    e1 = Edge(Vertex(1), Vertex(2))
    assert e1.Adj(Vertex(1)) == 2
    assert e1.Adj(Vertex(2)) == 1
    assert e1.Adj(Vertex(3)) is None

def test_set():
    s = set([(1, 2), (3, 2), (2, 1), (1, 2)])
    s |= set([(2, 3)])
    s |= set([1, 2])

def test_GraphCtr1():
    g = Graph([Edge(Vertex(1), Vertex(2))])
    assert g.E[0][0] == 1 and g.E[0][1] == 2


def test_GraphCtr2():
    g = Graph([
        Edge(Vertex(1), Vertex(2)),
        Edge(Vertex(3), Vertex(2))
    ])
    assert g.E[0][0] == 1 and g.E[0][1] == 2
    assert g.E[1][0] == 2 and g.E[1][1] == 3
    

def test_Graph__add__():
    g = Graph()
    e = Edge(Vertex(1), Vertex(2))
    g = g + e
    assert g.E[0][0] == 1
    assert g.E[0][1] == 2

def test_Graph__iadd__():
    g = Graph()
    e = Edge(Vertex(1), Vertex(2))
    g += e
    assert g.E[0][0] == 1
    assert g.E[0][1] == 2


def test_GraphV1():
    g = Graph([
        Edge(Vertex(1), Vertex(2)),
        Edge(Vertex(3), Vertex(2))
    ])
    assert g.V == [Vertex(1), Vertex(2), Vertex(3)]

def test_GraphV2():
    g = Graph([
        Edge(Vertex(1), Vertex(2)),
        Edge(Vertex(3), Vertex(2))
    ])
    g.V[0].discovered = True
    assert g.V[0].discovered == True and g.V[1].discovered == False and g.V[2].discovered == False

# def test_Adj1():
#     g = Graph([
#         Edge(Vertex(1), Vertex(2)),
#         Edge(Vertex(3), Vertex(2)),
#         Edge(Vertex(3), Vertex(5)),
#         Edge(Vertex(4), Vertex(3))
#     ])
#     assert g.AdjV(Vertex(3)) == [2, 4, 5]
#     assert g.AdjV(Vertex(1)) == [2]
#     assert g.AdjV(Vertex(2)) == [1, 3]


def test_AdjE():
    edges = [Edge(Vertex(1), Vertex(2)),
             Edge(Vertex(3), Vertex(2)),
             Edge(Vertex(3), Vertex(5)),
             Edge(Vertex(4), Vertex(3))]
    g = Graph(edges)
    assert g.AdjE(edges[0]) == [edges[1]]

def test_V_VertexId():
    v0 = Vertex(1)
    v1 = Vertex(2)
    g = Graph([Edge(v0, v1)])
    assert g.V[0] is v0
    assert g.V[1] is v1


# def test_discoverContinents1():
#     g = Graph([
#         Edge(Vertex(1), Vertex(2)),
#         Edge(Vertex(2), Vertex(3)),
#         Edge(Vertex(3), Vertex(1))
#     ])
#     g.discoverContinents()
#     assert len(g.C) == 1 and len(g.C[0].vertices) == 3


def test_discoverContinentsE1():
    g = Graph([
        Edge(Vertex(1), Vertex(2)),
        Edge(Vertex(2), Vertex(3)),
        Edge(Vertex(3), Vertex(1))
    ])
    g.discoverContinents()
    assert len(g.C) == 1 and len(g.C[0].E) == 3

# def test_discoverContinents2():
#     g = Graph([
#         Edge(Vertex(1), Vertex(2)),
#         Edge(Vertex(2), Vertex(3)),
#         Edge(Vertex(3), Vertex(1)),
#         Edge(Vertex(3), Vertex(4)),
#         Edge(Vertex(4), Vertex(5)),
#         Edge(Vertex(5), Vertex(6)),
#         Edge(Vertex(4), Vertex(6))
#     ])
#     g.discoverContinents()
#     assert len(g.C) == 1 and len(g.C[0].vertices) == 6


def test_discoverContinentsE2():
    g = Graph([
        Edge(Vertex(1), Vertex(2)),
        Edge(Vertex(2), Vertex(3)),
        Edge(Vertex(3), Vertex(1)),
        Edge(Vertex(3), Vertex(4)),
        Edge(Vertex(4), Vertex(5)),
        Edge(Vertex(5), Vertex(6)),
        Edge(Vertex(4), Vertex(6))
    ])
    g.discoverContinents()
    assert len(g.C) == 1 and len(g.C[0].E) == 7


# def test_discoverContinents3():
#     g = Graph([
#         Edge(Vertex(1), Vertex(2)),
#         Edge(Vertex(2), Vertex(3)),
#         Edge(Vertex(3), Vertex(1)),
#         Edge(Vertex(3), Vertex(4)),
#         Edge(Vertex(4), Vertex(5)),
#         Edge(Vertex(5), Vertex(6)),
#         Edge(Vertex(4), Vertex(6)),
#         Edge(Vertex(7), Vertex(8))
#     ])
#     g.discoverContinents()
#     assert len(g.C) == 2
#     assert len(g.C[0].vertices) == 6
#     assert len(g.C[1].vertices) == 2


def test_discoverContinentsE3():
    g = Graph([
        Edge(Vertex(1), Vertex(2)),
        Edge(Vertex(2), Vertex(3)),
        Edge(Vertex(3), Vertex(1)),
        Edge(Vertex(3), Vertex(4)),
        Edge(Vertex(4), Vertex(5)),
        Edge(Vertex(5), Vertex(6)),
        Edge(Vertex(4), Vertex(6)),
        Edge(Vertex(7), Vertex(8))
    ])
    g.discoverContinents()
    assert len(g.C) == 2
    assert len(g.C[0].E) == 7
    assert len(g.C[1].E) == 1


def test_Codingame():
    g = Graph([
        Edge(Vertex(4), Vertex(10)),
        Edge(Vertex(7), Vertex(2)),
        Edge(Vertex(2), Vertex(1)),
        Edge(Vertex(4), Vertex(1)),
        Edge(Vertex(8), Vertex(10)),
        Edge(Vertex(3), Vertex(9)),
        Edge(Vertex(6), Vertex(3)),
        Edge(Vertex(8), Vertex(0)),
        Edge(Vertex(7), Vertex(4)),
        Edge(Vertex(5), Vertex(10)),
        Edge(Vertex(9), Vertex(6)),
        Edge(Vertex(7), Vertex(0)),
        Edge(Vertex(8), Vertex(5))
    ])
    g.discoverContinents()
    totTiles = sum([c.totalTiles for c in g.C])
    assert len(g.C) == 2
    assert totTiles == 4



# g = Graph([
#     Edge(Vertex(1), Vertex(2)),
#     Edge(Vertex(2), Vertex(3)),
#     Edge(Vertex(3), Vertex(1)),
#     Edge(Vertex(3), Vertex(4)),
#     Edge(Vertex(4), Vertex(5)),
#     Edge(Vertex(5), Vertex(6)),
#     Edge(Vertex(4), Vertex(6)),
#     Edge(Vertex(7), Vertex(8))
# ])
# g.E
# d = [g.E[0], g.E[1]]
# d
# g.E[0] in d
# d
# g.E[5]
        
# g.E[5] in d
# id(d[0])
# id(d[1])
# id(g.E[5])
# d

# e = [[1,2], [2,3]]
# [1,2] in e
# [4,5] in e
