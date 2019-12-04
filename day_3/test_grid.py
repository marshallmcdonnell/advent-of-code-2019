import pytest
from wire import Wire
from grid import Grid

@pytest.fixture
def wire_one():
    instructions = "R8,U5,L5,D3"
    return Wire(instructions)

@pytest.fixture
def wire_two():
    instructions = "U7,R6,D4,L4"
    return Wire(instructions)

def test_construction():
    grid = Grid()
    assert not grid.wires

def test_construction_with_one_wire(wire_one):
    grid = Grid(wire_one)
    assert grid.wires == [wire_one]

def test_construction_with_multi_wires(wire_one, wire_two):
    wires = [wire_one, wire_two]
    grid = Grid(wires)
    assert grid.wires == wires

def test_manhattan_distance():
    assert Grid.manhattan_distance((2,2),(3,3)) == 2
    assert Grid.manhattan_distance((2,2,2),(3,3,3)) == 3

def test_compute_instersections(wire_one, wire_two):
    wires = [wire_one, wire_two]
    grid = Grid(wires)
    grid._compute_intersections()
    assert grid.intersections == [(3,3), (6,5)]

def test_closest_intersection(wire_one, wire_two):
    wires = [wire_one, wire_two]
    grid = Grid(wires)
    assert grid.closest_intersection == (3,3)


def test_closest_intersection_distance(wire_one, wire_two):
    wires = [wire_one, wire_two]
    grid = Grid(wires)
    assert grid.closest_intersection_distance == 6
