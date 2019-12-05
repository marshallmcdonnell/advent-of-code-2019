import argparse
import itertools

def expand_ints(s):
    spans = (el.partition('-')[::2] for el in s.split(','))
    ranges = (range(int(s), int(e) + 1 if e else int(s) + 1)
              for s, e in spans)
    all_nums = itertools.chain.from_iterable(ranges)
    return list(all_nums)

class PasswordValidator:
    def __init__(self, passwords=None):
        self._passwords = []

        if passwords:
            for p in passwords:
                self.add_password(p)

    @staticmethod
    def convert_password_to_list(password):
        return list(map(int, str(password)))

    @classmethod
    def validate_password_length(cls, password, length=6):
        password_list = cls.convert_password_to_list(password)
        return len(password_list) == length
        

    @classmethod
    def validate_two_adjacent_digits(cls, password):
        password_list = cls.convert_password_to_list(password)
        password_set = set(password_list)
        return len(password_set) < len(password_list) 

    @classmethod
    def validate_not_decreasing(cls, password):
        password_list = cls.convert_password_to_list(password)
        return password_list == sorted(password_list)

    def add_password(self, password):
        self._passwords.append(password)

    @classmethod
    def validate_repeated_elements(cls, password, repeated=2):

        password_list = cls.convert_password_to_list(password)
        for a in password_list:
            list_copy = password_list.copy()
            for b in list_copy:
                if a in list_copy:
                    list_copy.remove(a)
            if len(list_copy) == len(password_list) - repeated:
                return True
        return False
            

    @property
    def number_of_valid_passwords_part_one(self):
        number_valid = 0
        for p in self.passwords:
            valid = self.validate_password_length(p)
            valid = self.validate_two_adjacent_digits(p) & valid 
            valid = self.validate_not_decreasing(p) & valid
            if valid:
                number_valid += 1
        return number_valid

    @property
    def number_of_valid_passwords_part_two(self):
        number_valid = 0
        for p in self.passwords:
            valid = self.validate_password_length(p)
            valid = self.validate_two_adjacent_digits(p) & valid 
            valid = self.validate_not_decreasing(p) & valid
            valid = self.validate_repeated_elements(p) & valid
            if valid:
                number_valid += 1
        return number_valid

    @property
    def passwords(self):
        return self._passwords

if __name__ == "__main__":
    # Parse CLI arguements
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=str,
                        help="Input string for range (ie '1-5' for 1,2,3,4,5).")
    parser.add_argument("--part", type=int, default=1,
                        choices=[1, 2],
                        help="Either sovling part 1 or part 2 of problem")
    args = parser.parse_args()

    passwords = expand_ints(args.input)
    pv = PasswordValidator(passwords)
    if args.part == 1:
        print("Number of valid passwords (Part 1): {}".format(pv.number_of_valid_passwords_part_one))
    if args.part == 2:
        print("Number of valid passwords (Part 2): {}".format(pv.number_of_valid_passwords_part_two))
