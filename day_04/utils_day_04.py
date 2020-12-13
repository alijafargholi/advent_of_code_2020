id_keys = [
    "byr",  # (Birth Year)
    "iyr",  # (Issue Year)
    "eyr",  # (Expiration Year)
    "hgt",  # (Height)
    "hcl",  # (Hair Color)
    "ecl",  # (Eye Color)
    "pid",  # (Passport ID)
    # "cid",  # (Country ID)  # this is not required, we can ignore it
]


def get_clean_data():
    with open("input.txt") as input_file:
        lines = input_file.read()
        data = [_.replace("\n", " ").split() for _ in lines.split("\n\n")]
        passport_data = []
        for _id in data:
            passport_data.append({_.split(":")[0]: _.split(":")[1] for _ in _id})

    return  passport_data
