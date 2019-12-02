import pytest
from intcode import IntCode, UnknownOpCode


def test_construction():
    input_code = [1, 0, 0, 3, 99]
    intcode = IntCode(input_code)
    assert intcode.ADD == 1
    assert intcode.MULTIPLY == 2
    assert intcode.HALT == 99
    assert intcode.OPCODE_CHOICES == ['1', '2', '99']
    assert intcode._stride == 4
    assert intcode._number_of_commands == 2

    assert intcode._input == input_code
    input_code[0] = 9
    assert intcode._input != input_code


def test_product():
    assert IntCode.product([1, 2, 3, 4]) == 24


def test_create_list_from_positions():
    input_code = [1, 0, 0, 3, 99]
    intcode = IntCode(input_code)
    assert intcode._create_list_from_positions([0, 2, 4]) == [1, 0, 99]


def test_run_add_simple():
    input_code = [1, 0, 0, 3, 99]
    intcode = IntCode(input_code)

    pos1 = input_code[1]
    pos2 = input_code[2]
    output_position = input_code[3]
    positions = [pos1, pos2]

    intcode._run_add(positions, output_position)
    assert intcode._input == [1, 0, 0, 2, 99]


def test_run_add_complex():
    input_code = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
    intcode = IntCode(input_code)

    pos1 = input_code[1]
    pos2 = input_code[2]
    output_position = input_code[3]
    positions = [pos1, pos2]

    intcode._run_add(positions, output_position)
    assert intcode._input == [1, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]


def test_run_multiply_simple():
    input_code = [3, 0, 0, 3, 99]
    intcode = IntCode(input_code)

    pos1 = input_code[1]
    pos2 = input_code[2]
    output_position = input_code[3]
    positions = [pos1, pos2]

    intcode._run_multiply(positions, output_position)
    assert intcode._input == [3, 0, 0, 9, 99]


def test_run_multiply_complex():
    input_code = [1, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
    intcode = IntCode(input_code)

    pos1 = input_code[5]
    pos2 = input_code[6]
    output_position = input_code[7]
    positions = [pos1, pos2]

    intcode._run_multiply(positions, output_position)
    assert intcode._input == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]


def test_output():
    input_code = [1, 0, 0, 3, 99]
    intcode = IntCode(input_code)
    assert intcode._output() == "1,0,0,3,99"


def test_run_commands_complex():
    input_code = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
    intcode = IntCode(input_code)
    intcode.run_commands()
    assert intcode._input == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]


def test_run_commands_simple_test_0():
    input_code = [1, 0, 0, 3, 99]
    intcode = IntCode(input_code)
    intcode.run_commands()
    assert intcode._input == [1, 0, 0, 2, 99]


def test_run_commands_simple_test_1():
    input_code = [1,0,0,0,99]
    intcode = IntCode(input_code)
    intcode.run_commands()
    assert intcode._input == [2,0,0,0,99]


def test_run_commands_simple_test_2():
    input_code = [2,3,0,3,99]
    intcode = IntCode(input_code)
    intcode.run_commands()
    assert intcode._input == [2,3,0,6,99]


def test_run_commands_simple_test_3():
    input_code = [2,4,4,5,99,0]
    intcode = IntCode(input_code)
    intcode.run_commands()
    assert intcode._input == [2,4,4,5,99,9801]


def test_run_commands_simple_test_4():
    input_code = [1,1,1,4,99,5,6,0,99]
    intcode = IntCode(input_code)
    intcode.run_commands()
    assert intcode._input == [30,1,1,4,2,5,6,0,99]

def test_run_commands_invalid_opcode():
    input_code = [5,0,0,0,99]
    intcode = IntCode(input_code)
    with pytest.raises(UnknownOpCode):
        intcode.run_commands()
