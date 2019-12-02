import argparse
import operator
from functools import reduce


class UnknownInstruction(Exception):
    ''' Raise if we come accross an unknown INSTRUCTION '''


class IntCode:
    ''' IntCode class for computing series of Instructions '''

    # INSTRUCTIONS
    ADD = 1
    MULTIPLY = 2
    HALT = 99
    INSTRUCTION_CHOICES = [str(x) for x in [ADD, MULTIPLY, HALT]]

    def __init__(self, command_list, stride=4):
        ''' Initialize object of IntCode with instruction command list
        and a stride for the command length (default: 4)
        :param command_list: List of instructions to execute
        :type command_list: list[int]
        :param stride: Length of the commands with structure:
                       [instruction, pos1, pos2, ..., output_position]
        :type stride: int
        '''
        self._stride = stride
        self._memory = [int(x) for x in command_list]
        self._number_of_commands = int(len(self._memory) / stride) + 1

    @staticmethod
    def product(value_list):
        ''' Static method used to compute produce of a list of values.
        :param value_list: List of floats to compute product
        :type value_list: list[float]
        :return: Produce of list (ie [1,2,3] = 1 * 2 * 3 = 6)
        :rtype: float
        '''
        return reduce(operator.mul, value_list)

    def _create_list_from_positions(self, positions):
        ''' Create a value list from a list of positions in the commands
        list (ie IntCode._memory)
        :param positions: List of positions to create value list from
        :type positions: list[int]
        :return: List of values that correspond to the positions
        :rtype: list[float]
        '''
        value_list = []
        for p in positions:
            value = self._memory[p]
            value_list.append(value)
        return value_list

    def _run_add(self, positions, output_position):
        ''' Add the values together that are at the positions given
        in the commands list and store them in the output position
        given in the commands list
        :param positions: Positions for corresponding values to compute sum
        :type positions: list[int]
        :param output_position: Position to store summation in commands list
        :type output_position: int
        '''
        value_list = self._create_list_from_positions(positions)
        self._memory[output_position] = sum(value_list)

    def _run_multiply(self, positions, output_position):
        ''' Multiply the values together that are at the positions given
        in the commands list and store them in the output position
        given in the commands list
        :param positions: Positions for corresponding values to compute product
        :type positions: list[int]
        :param output_position: Position to store product in commands list
        :type output_position: int
        '''
        value_list = self._create_list_from_positions(positions)
        self._memory[output_position] = self.product(value_list)

    def _output(self):
        ''' Return current command list as a comma-separated string '''
        return ",".join([str(x) for x in self._memory])        

    def run_commands(self):
        ''' Run the commands input into IntCode object and return
        the output upon reaching the halt command
        '''
        for i in range(self._number_of_commands):
            start = i * self._stride
            stop = start + self._stride
            command = self._memory[start:stop]

            instruction = command[0]
            parameters = command[1:-1]
            output_position = command[-1]

            if instruction == self.ADD:
                self._run_add(parameters, output_position)

            elif instruction == self.MULTIPLY:
                self._run_multiply(parameters, output_position)

            elif instruction == self.HALT:
                return self._output()

            else:
                msg = "Unknown INSTRUCTION: {} Choices: {}"
                msg = msg.format(instruction, ','.join(self.INSTRUCTION_CHOICES))
                raise UnknownInstruction(msg)


if __name__ == "__main__":
    # Parse CLI arguements
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str,
                        help="Input file with list of instructions.")
    parser.add_argument("--part", type=int, default=1,
                        choices=[1, 2],
                        help="Either sovling part 1 or part 2 of problem")
    args = parser.parse_args()

    # Read in input file with list of masses and parse
    with open(args.input_file, 'r') as f:
        contents = f.readline()
    code = [int(x.strip()) for x in contents.split(',')]

    if args.part == 1:
        # Initialize IntCode object
        intcode = IntCode(code)

        # Replace the values per the instructions
        intcode._memory[1] = 12
        intcode._memory[2] = 2

        # Print output to screen for the solution
        print("Output: {}".format(intcode.run_commands()))

    if args.part == 2:
        target = 19690720

        span = range(0,100)
        for noun in span:
            for verb in span:
                intcode = IntCode(code)
                intcode._memory[1] = noun
                intcode._memory[2] = verb

                intcode.run_commands()

                if intcode._memory[0] == target:
                    print("Hit target!!! Noun: {} Verb: {} 100*Noun+Verb: {}".format(noun, verb, 100*noun+verb))

