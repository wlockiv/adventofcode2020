import re
from typing import IO, Dict


def validate_passport(passport: Dict[str, str]) -> bool:
    def validate_hgt(h: str):
        val, unit = int(h[:-2]), h[-2:]
        if unit == 'in' and (59 <= val <= 76):
            return True
        elif unit == 'cm' and (150 <= val <= 193):
            return True

        return False

    def validate_ecl(ecl: str):
        valid_colors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
        return True if ecl in valid_colors else False

    passport_fields = {
        'byr': lambda x: 1920 <= int(x) <= 2002,
        'iyr': lambda x: 2010 <= int(x) <= 2020,
        'eyr': lambda x: 2020 <= int(x) <= 2030,
        'hgt': validate_hgt,
        'hcl': lambda x: bool(re.search('^#[0-9a-f]{6}$', x)),
        'ecl': validate_ecl,
        'pid': lambda x: bool(re.search('^[0-9]{9}$', x))
    }

    for key, fn in passport_fields.items():
        try:
            if not fn(passport[key]):
                return False
        except KeyError:
            return False

    return True


def parse_passport(passport: str):
    passport = passport.replace('\n', ' ')
    passport_split = passport.split(' ')

    parsed = {}

    for kv in passport_split:
        k, v = kv.split(':')
        parsed[k] = v

    return parsed


def main(input_file: IO):
    passports = input_file.read().split('\n\n')
    parsed_passports = [parse_passport(p) for p in passports]

    valid_passports = list(filter(validate_passport, parsed_passports))

    print('The answer for Day 04 Part B :', len(valid_passports))
