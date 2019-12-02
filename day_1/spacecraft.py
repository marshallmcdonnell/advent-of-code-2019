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
    return math.floor(mass / 3) - 2


def fuel_counter_upper_summation(masses):
    '''
    Determine fuel required for a module given its mass. Specifically,
    will divide mass by 3, round down, and subtract by 2.


    :param mass: Mass of the module to calculate fuel for
    :type mass: float
    :return: The fuel requirement for the input mass.
    :rtype: float
    '''
    output = []
    for mass in masses:
        fuel = fuel_counter_upper(mass)
        output.append(fuel)

    return sum(output)
