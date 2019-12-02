import spacecraft


def test_fuel_counter_upper():
    ''' Test for the basic fuel counter '''
    assert spacecraft.fuel_counter_upper(-2) == 0
    assert spacecraft.fuel_counter_upper(12) == 2
    assert spacecraft.fuel_counter_upper(14) == 2
    assert spacecraft.fuel_counter_upper(1969) == 654
    assert spacecraft.fuel_counter_upper(100756) == 33583


def test_fuel_counter_upper_recursive():
    ''' Test the recursive version of fuel counter '''
    assert spacecraft.fuel_counter_upper_recursive(12) == 2
    assert spacecraft.fuel_counter_upper_recursive(14) == 2
    assert spacecraft.fuel_counter_upper_recursive(1969) == 966
    assert spacecraft.fuel_counter_upper_recursive(100756) == 50346


def test_fuel_counter_upper_summation():
    ''' Test the summation version of fuel counter '''
    masses = [12, 14, 1969, 100756]
    target = 2 + 2 + 654 + 33583
    assert spacecraft.fuel_counter_upper_summation(masses) == target


def test_fuel_counter_upper_summation_recursive():
    ''' Test the summation version of fuel counter with recursion'''
    masses = [12, 14, 1969, 100756]
    target = 2 + 2 + 966 + 50346
    assert spacecraft.fuel_counter_upper_summation(
        masses, recursive=True) == target
