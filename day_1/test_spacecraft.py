import spacecraft


def test_fuel_counter_upper():
    assert spacecraft.fuel_counter_upper(12) == 2
    assert spacecraft.fuel_counter_upper(14) == 2
    assert spacecraft.fuel_counter_upper(1969) == 654
    assert spacecraft.fuel_counter_upper(100756) == 33583


def test_fuel_counter_upper_summation():
    assert spacecraft.fuel_counter_upper_summation([12, 14]) == 2 + 2
