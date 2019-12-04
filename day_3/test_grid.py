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

def test_closest_combined_step_distance(wire_one, wire_two):
    wires = [wire_one, wire_two]
    grid = Grid(wires)
    assert grid.closest_combined_step_distance == 30

    wire_one = Wire("R75,D30,R83,U83,L12,D49,R71,U7,L72")
    wire_two = Wire("U62,R66,U55,R34,D71,R55,D58,R83")
    grid = Grid([wire_one, wire_two])
    assert grid.closest_combined_step_distance == 610

    wire_one = Wire("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51")
    wire_two = Wire("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")
    grid = Grid([wire_one, wire_two])
    assert grid.closest_combined_step_distance == 410
def test_combined_step_distance(wire_one, wire_two):
    wires = [wire_one, wire_two]
    grid = Grid(wires)    
    assert Grid.combined_step_distance((3,3), wire_one.points) == 20 
    assert Grid.combined_step_distance((3,3), wire_two.points) == 20
    assert Grid.combined_step_distance((6,5), wire_one.points) == 15 
    assert Grid.combined_step_distance((6,5), wire_two.points) == 15
