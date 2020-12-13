"""
https://adventofcode.com/2020/day/4

--- Part Two ---
The line is moving more quickly now, but you overhear airport security talking
about how passports with invalid data are getting through. Better add some
data validation, quick!

You can continue to ignore the cid field, but each other field has strict rules
about what values are valid for automatic validation:

byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
Your job is to count the passports where all required fields are both present
and valid according to the above rules. Here are some example values:

byr valid:   2002
byr invalid: 2003

hgt valid:   60in
hgt valid:   190cm
hgt invalid: 190in
hgt invalid: 190

hcl valid:   #123abc
hcl invalid: #123abz
hcl invalid: 123abc

ecl valid:   brn
ecl invalid: wat

pid valid:   000000001
pid invalid: 0123456789
Here are some invalid passports:

eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
Here are some valid passports:

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
Count the number of valid passports - those that have all required fields and
valid values. Continue to treat cid as optional. In your batch file, how
many passports are valid?
"""
import re

import utils_day_04

hair_color_pattern = r"#[a-f|0-9]{6}$"
hair_color_compiled = re.compile(hair_color_pattern)

pid_pattern = r"[0-9]{9}$"
pid_pattern_compiled = re.compile(pid_pattern)

four_digit_pattern = r"[0-9]{4}$"
four_digit_pattern_compiled = re.compile(four_digit_pattern)

valid_passport = 0

all_passports = utils_day_04.get_clean_data()
for passport in all_passports:
    # making sure there are no missing id keys
    if not all(item in passport for item in utils_day_04.id_keys):
        continue

    birthday = passport.get("byr")
    issue_year = passport.get("iyr")
    expiration_year = passport.get("eyr")
    if not all(
            list(
                map(
                    four_digit_pattern_compiled.match,
                    [birthday, issue_year, expiration_year]
                )
            )
    ):
        continue

    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if not 1920 <= int(birthday) <= 2002:
        continue

    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    if not 2010 <= int(issue_year) <= 2020:
        continue

    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    if not 2020 <= int(expiration_year) <= 2030:
        continue

    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    height = passport.get("hgt")
    if "cm" not in height and "in" not in height:
        continue

    if height.endswith("cm"):
        height_cm = int(height.strip("cm"))
        if not 150 <= height_cm <= 193:
            continue

    if height.endswith("in"):
        height_in = int(height.strip("in"))
        if not 59 <= height_in <= 76:
            continue

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    if not hair_color_compiled.match(passport.get("hcl")):
        continue

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    if passport.get("ecl") not in "amb blu brn gry grn hzl oth".split():
        continue

    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    passport_id = passport.get("pid")
    if not pid_pattern_compiled.match(passport_id):
        continue

    valid_passport += 1

print("Total passports are: {}, but only {} passports are valid".format(
    len(all_passports), valid_passport
))  # Total passports are: 290, but only 172 passports are valid
