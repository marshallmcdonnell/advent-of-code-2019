from secure import expand_ints, PasswordValidator

def test_expand_ints():
    s = "1-3, 8-9, 12"
    assert expand_ints(s) == [1,2,3,8,9,12]

def test_construction():
    pv = PasswordValidator()
    assert not pv.passwords


def test_construction_with_passwords():
    password = 111111
    pv = PasswordValidator(passwords=[password])
    assert pv.passwords == [password]


def test_add_password():
    password = 111111
    pv = PasswordValidator()
    pv.add_password(password)
    assert pv.passwords == [password]


def test_convert_password_to_list():
    password = 111111
    target = [1, 1, 1, 1, 1, 1]
    assert PasswordValidator.convert_password_to_list(password) == target


def test_validate_password_length():
    password = 123456
    assert PasswordValidator.validate_password_length(password) == True
    assert PasswordValidator.validate_password_length(password, length=6) == True
    assert PasswordValidator.validate_password_length(password, length=5) == False

    password = 12345
    assert PasswordValidator.validate_password_length(password) == False
    assert PasswordValidator.validate_password_length(password, length=6) == False
    assert PasswordValidator.validate_password_length(password, length=5) == True

    password = 1234567
    assert PasswordValidator.validate_password_length(password) == False
    assert PasswordValidator.validate_password_length(password, length=6) == False
    assert PasswordValidator.validate_password_length(password, length=7) == True


def test_validate_two_adjacent_digits():
    password = 111111
    assert PasswordValidator.validate_two_adjacent_digits(password) == True

    password = 123455
    assert PasswordValidator.validate_two_adjacent_digits(password) == True

    password = 223450
    assert PasswordValidator.validate_two_adjacent_digits(password) == True 

    password = 123789
    assert PasswordValidator.validate_two_adjacent_digits(password) == False


def test_validate_not_decreasing():
    password = 111111
    assert PasswordValidator.validate_not_decreasing(password) == True

    password = 123455
    assert PasswordValidator.validate_not_decreasing(password) == True

    password = 223450 
    assert PasswordValidator.validate_not_decreasing(password) == False

    password = 123789
    assert PasswordValidator.validate_not_decreasing(password) == True


def test_validate_repeated_elements():
    password = 112233
    assert PasswordValidator.validate_repeated_elements(password) == True
        
    password = 123444
    assert PasswordValidator.validate_repeated_elements(password) == False

    password = 111122
    assert PasswordValidator.validate_repeated_elements(password) == True


def test_number_of_valid_passwords_part_one():
    passwords = [111111, 223450, 123789]
    pv = PasswordValidator(passwords)
    assert pv.number_of_valid_passwords_part_one == 1


def test_number_of_valid_passwords_part_two():
    passwords = [112233, 123444, 111122]
    pv = PasswordValidator(passwords)
    assert pv.number_of_valid_passwords_part_two == 2
