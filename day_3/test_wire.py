import pytest

from wire import Wire, UnknownDirectionException, InvalidInstructionFormat


def test_construction():
    wire = Wire()
    assert wire.RIGHT == 'R'
    assert wire.LEFT == 'L'
    assert wire.UP == 'U'
    assert wire.DOWN == 'D'
    assert wire.SHIFT_RIGHT == (1, 0)
    assert wire.SHIFT_LEFT == (-1, 0)
    assert wire.SHIFT_UP == (0, 1)
    assert wire.SHIFT_DOWN == (0, -1)
    assert not wire.instructions
    assert wire.points == [(0, 0)]


def test_construction_with_instructions():
    instructions = "U2,L2"
    wire = Wire(instructions)
    assert wire.instructions == instructions
    #  assert wire.points == [(1,0), (2,0), (2,1), (2,2)]

    instructions = "U2,L2"
    wire = Wire()
    wire.instructions = instructions
    assert wire.instructions == instructions
    #  assert wire.points == [(1,0), (2,0), (2,1), (2,2)]


def test_add_points():
    wire = Wire()
    assert wire.add_points((4, 4), (1, 1)) == (5, 5)


def test_direction_to_point():
    wire = Wire()
    assert wire._direction_to_point(wire.RIGHT) == (1, 0)

    wire = Wire()
    assert wire._direction_to_point(wire.LEFT) == (-1, 0)

    wire = Wire()
    assert wire._direction_to_point(wire.UP) == (0, 1)

    wire = Wire()
    assert wire._direction_to_point(wire.DOWN) == (0, -1)

    with pytest.raises(UnknownDirectionException):
        wire = Wire()
        wire._direction_to_point('Q')


def test_points_from_single_instruction():
    wire = Wire()
    wire._extend_points_from_single_instruction("U2")
    assert wire.points == [(0, 0), (0, 1), (0, 2)]

    wire = Wire()
    with pytest.raises(InvalidInstructionFormat):
        wire._extend_points_from_single_instruction("")
    with pytest.raises(InvalidInstructionFormat):
        wire._extend_points_from_single_instruction("U")
    with pytest.raises(InvalidInstructionFormat):
        wire._extend_points_from_single_instruction("U2D")
    with pytest.raises(InvalidInstructionFormat):
        wire._extend_points_from_single_instruction("U2,")
    with pytest.raises(InvalidInstructionFormat):
        wire._extend_points_from_single_instruction("U2,D2")


def test_points_from_instructions():
    wire = Wire()
    wire.extend_points_from_instructions("U2")
    assert wire.points == [(0, 0), (0, 1), (0, 2)]

    wire = Wire()
    wire.extend_points_from_instructions("U2,R2")
    assert wire.points == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]
