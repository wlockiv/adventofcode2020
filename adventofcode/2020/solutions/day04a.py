from typing import IO


def validate_passport(passport) -> bool:
    passport_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    for field in passport_fields:
        if field not in passport:
            return False

    return True


def main(input_file: IO):
    passports = input_file.read().split('\n\n')

    valid_passports = list(filter(validate_passport, passports))

    print('The answer for Day 04 Part A :', len(valid_passports))
