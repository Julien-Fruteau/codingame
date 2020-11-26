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
    assert e1.a == 1
    assert e2.a == 2
    assert e3.a == 2

def test_set():
    s = set([(1, 2), (3, 2), (2, 1), (1, 2)])
    s |= set([(2, 3)])
    s |= set([1, 2])

def test_GraphCtr():
    g = Graph([Edge(Vertex(1), Vertex(2))])
    assert g.E[0].a == 1
    assert g.E[0].b == 2

def test_Graph__add__():
    g = Graph()
    e = Edge(Vertex(1), Vertex(2))
    g = g + e
    assert g.E[0].a == e.a
    assert g.E[0].b == e.b

def test_Graph__iadd__():
    g = Graph()
    e = Edge(Vertex(1), Vertex(2))
    g += e
    assert g.E[0].a == e.a
    assert g.E[0].b == e.b
