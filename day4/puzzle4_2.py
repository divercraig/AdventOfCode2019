
def contains_exactly_two_adjacent_identical_digits(digits: int):
    string_version = str(digits)
    adjacent_chars = set()
    previous_char = string_version[0]
    for char in string_version[1:]:
        if char == previous_char:
            adjacent_chars.add(char)
        previous_char = char

    double_char = False
    if len(adjacent_chars) > 0:
        for char in adjacent_chars:
            triple_char = char + char + char
            if triple_char not in string_version:
                double_char = True

    return double_char


def never_decreasing_digits(digits: int):
    string_version = str(digits)
    decreased = False
    previous_digit = int(string_version[0])
    for char in string_version[1:]:
        if int(char) < previous_digit:
            decreased = True
            break
        previous_digit = int(char)

    return not decreased


def check_rules(digits: int):
    if never_decreasing_digits(digits) and contains_exactly_two_adjacent_identical_digits(digits):
        return True


password_lower = 206938
password_upper = 679128

potential_passwords = 0
full_count = 0

for a in range(password_lower, password_upper):
    full_count += 1
    if check_rules(a):
        potential_passwords += 1

print ("{} potential passwords out of {} range".format(potential_passwords, full_count))