import argparse
import math


def fuel_counter_upper(mass):
    '''
    Determine fuel required for a module given its mass. Specifically,
    will divide mass by 3, round down, and subtract by 2.


    :param mass: Mass of the module to calculate fuel for
    :type mass: float
    :return: The fuel requirement for the input mass.
    :rtype: float
    '''
    fuel = math.floor(mass / 3) - 2
    if fuel < 0:
        fuel = 0
    return fuel


def fuel_counter_upper_recursive(mass, total_fuel=0):
    '''
    Determine fuel required for a module given its mass. Specifically,
    will divide mass by 3, round down, and subtract by 2. Also,
    calculate the additional fuel for the additional fuel's mass.
    Recursively calculates till we reach a infinitesimal mass of fuel.


    :param mass: Mass of the module to calculate fuel for
    :type mass: float
    :param total_fuel: Running total of fuel requirement (default=0)
    :type total_fuel: float
    :return: The fuel requirement for the input mass.
    :rtype: float
    '''
    fuel = fuel_counter_upper(mass)
    total_fuel += fuel

    if fuel <= 0:
        return total_fuel
    else:
        return fuel_counter_upper_recursive(fuel, total_fuel)


def fuel_counter_upper_summation(masses, recursive=False):
    '''
    Determine fuel required for a module given its mass. Specifically,
    will divide mass by 3, round down, and subtract by 2.


    :param mass: Mass of the module to calculate fuel for
    :type mass: float
    :param recursive: Boolean flag to run recursive version
                      for accounting for additional fuel's mass.
    :type recursive: bool
    :return: The fuel requirement for the input mass.
    :rtype: float
    '''
    output = []
    for mass in masses:
        if recursive:
            fuel = fuel_counter_upper_recursive(mass)
        else:
            fuel = fuel_counter_upper(mass)

        output.append(fuel)

    return sum(output)


if __name__ == "__main__":
    # Parse CLI arguements
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str,
                        help="Input file with list of module masses.")
    parser.add_argument("--part", type=int, default=1,
                        choices=[1, 2],
                        help="Either sovling part 1 or part 2 of problem")
    args = parser.parse_args()

    # Read in input file with list of masses and parse
    with open(args.input_file, 'r') as f:
        contents = f.readlines()
    masses = [float(x.strip()) for x in contents]

    # Determine if we are solving Part I or Part II of the problem
    if args.part == 1:
        recursive = False
    elif args.part == 2:
        recursive = True

    # Calculate and output solution to problem
    fuel = fuel_counter_upper_summation(masses, recursive=recursive)
    print("Total fuel required: {}".format(fuel))
