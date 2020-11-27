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
    assert e1.getAdj(Vertex(1)) == 2
    assert e1.getAdj(Vertex(2)) == 1
    assert e1.getAdj(Vertex(3)) is None

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

def test_Adj1():
    g = Graph([
        Edge(Vertex(1), Vertex(2)),
        Edge(Vertex(3), Vertex(2)),
        Edge(Vertex(3), Vertex(5)),
        Edge(Vertex(4), Vertex(3))
    ])
    assert g.Adj(Vertex(3)) == [2, 4, 5]
    assert g.Adj(Vertex(1)) == [2]
    assert g.Adj(Vertex(2)) == [1, 3]
