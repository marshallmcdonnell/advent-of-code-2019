import re
from operator import add


class UnknownDirectionException(Exception):
    ''' Raised for unknown direction '''

class InvalidInstructionFormat(Exception):
    ''' Raised if an invalid instruction is found '''

class Wire:
    RIGHT = 'R'
    LEFT = 'L'
    UP = 'U'
    DOWN = 'D'
    DIRECTION_CHOICES = [RIGHT, LEFT, UP, DOWN]

    SHIFT_RIGHT = (1, 0)
    SHIFT_LEFT = (-1, 0)
    SHIFT_UP = (0, 1)
    SHIFT_DOWN = (0, -1)

    def __init__(self, wire_instructions=None):
        self._instructions = ""
        self._points = [(0, 0)]

        instruction_format = r"^[A-Z]\d+$"
        self._instruction_regex = re.compile(instruction_format)

        if wire_instructions:
            self.instructions = wire_instructions

    def extend_points_from_instructions(self, instructions):
        for instruction in instructions.split(','):
            self._extend_points_from_single_instruction(instruction)

    def _extend_points_from_single_instruction(self, instruction):
        if not self._instruction_regex.match(instruction):
            msg = "Invalid instruction: {}".format(instruction)
            raise InvalidInstructionFormat(msg)

        direction = instruction[0]
        iterations = int(instruction[1:])

        for i in range(1, iterations + 1):
            point = self._direction_to_point(direction)
            self._points.extend([point])

    def _direction_to_point(self, direction):
        if direction == self.RIGHT:
            point = self.add_points(self.last_point, self.SHIFT_RIGHT)
        elif direction == self.LEFT:
            point = self.add_points(self.last_point, self.SHIFT_LEFT)
        elif direction == self.UP:
            point = self.add_points(self.last_point, self.SHIFT_UP)
        elif direction == self.DOWN:
            point = self.add_points(self.last_point, self.SHIFT_DOWN)
        else:
            msg = "Direction: {} Choices: {}"
            msg = msg.format(direction, ','.join(self.DIRECTION_CHOICES))
            raise UnknownDirectionException(msg)
        return point

    @staticmethod
    def add_points(point1, point2):
        return tuple(map(add, point1, point2))

    @property
    def instructions(self):
        return self._instructions

    @instructions.setter
    def instructions(self, instructions):
        self._instructions = instructions
        self._points = self.extend_points_from_instructions(instructions)

    @property
    def points(self):
        return self._points

    @property
    def last_point(self):
        return self._points[-1]
