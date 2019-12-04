import re
from operator import add


class UnknownDirectionException(Exception):
    ''' Raised for unknown direction '''


class InvalidInstructionFormat(Exception):
    ''' Raised if an invalid instruction is found '''


class Wire:
    ''' Wire class for creating list of points for a given
    wire's instructions
    '''
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
        ''' Construction for a Wire object

        :param wire_instructions: Instructions for creating wire's path
                                  Example: "U2,D3,R1,L4" for a path of
                                  Up by 2, Down by 3, Right by 1, and Left by 4
        :type wire_instructions: str
        '''
        self._instructions = ""
        self._points = [(0, 0)]

        instruction_format = r"^[DLRU]\d+$"
        self._instruction_regex = re.compile(instruction_format)

        if wire_instructions:
            self.instructions = wire_instructions

    @staticmethod
    def add_points(point1, point2):
        ''' Add two points element-wise to create a new point (tuple).
        So, for point1=(3,4) and point2=(5,1), the new point will be
        (3+5, 4+1) = (8,5).

        :param point1: First point to add
        :type point1: tuple(int, int)
        :param point2: Second point to add
        :type point2: tuple(int, int)
        :return: New point from element-wise sum as a tuple(int, int)
        '''
        return tuple(map(add, point1, point2))

    def _direction_to_point(self, direction):
        '''Takes a direction instruction and creates a new point
        using the last point added to the Wire

        :param direction: String with direction instructions.
                          Choices: "U", "D", "R", "L"
                          Suggested to use the Wire class constants
                          UP, DOWN, RIGHT, and LEFT (ie Wire.UP)
        :type direction: str
        :return: tuple
        '''

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

    def _extend_points_from_single_instruction(self, instruction):
        ''' Extend / add new points to the wire from a single instruction,
        such as "U22" or "D5". These will add 22 and 5 new points,
        respectively, to the Wire object.

        :param instruction: Single instruction string
                            with format "[UDLR][0-9]+"
        :type instruction: str
        '''
        if not self._instruction_regex.match(instruction):
            msg = "Invalid instruction: {}".format(instruction)
            raise InvalidInstructionFormat(msg)

        direction = instruction[0]
        iterations = int(instruction[1:])

        for i in range(1, iterations + 1):
            point = self._direction_to_point(direction)
            self._points.extend([point])

    def extend_points_from_instructions(self, instructions):
        ''' Extend / add new points to the wire from a set of instructions,
        such as "U22,D5". These will add 27 new points to the Wire object.

        :param instructions: Comma-separated list of instructions.
                             Example: "L2,R5,D1"
        :type instructions: str
        '''
        for instruction in instructions.split(','):
            self._extend_points_from_single_instruction(instruction)

    @property
    def instructions(self):
        ''' Gets the current instruction set for the Wire '''
        return self._instructions

    @instructions.setter
    def instructions(self, instructions):
        ''' Sets the instructions and corresponding points to the Wire '''
        self._instructions = instructions
        self._points = self.extend_points_from_instructions(instructions)

    @property
    def points(self):
        ''' Gets the current points for the Wire '''
        return self._points

    @property
    def last_point(self):
        ''' Gets the last point added to the Wire '''
        return self._points[-1]
