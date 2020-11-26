import pytest
from src.puzzle_of_the_week.the_lost_files.classes import Graph, Vertex, Edge

def test_Edge():
    e1 = Edge(*(1, 2))
    e2 = Edge(*[2, 2])
    e3 = Edge(*[3, 2])
    assert e1.a == 1
    assert e2.a == 2
    assert e3.a == 2


def test_set():
    s = set([(1, 2), (3, 2), (2, 1), (1, 2)])
    s |= set([(2, 3)])
    s |= set([1, 2])

def test_GraphCtr():
    g = Graph([Edge(1, 2)])
    assert g.E[0].a == 1
    assert g.E[0].b == 2

def test_Graph__add__():
    g = Graph()
    e = Edge(1, 2)
    g = g + e
    assert g.E[0].a == e.a
    assert g.E[0].b == e.b

def test_Graph__iadd__():
    g = Graph()
    e = Edge(1, 2)
    g += e
    assert g.E[0].a == e.a
    assert g.E[0].b == e.b

