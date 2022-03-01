from collections import deque


def compare_each(char1, char2):
    if not char1:
        return True
    elif not char2:
        return False
    elif char1 == ".":
        return True
    elif char1 == char2:
        return True
    return False


def compare_equal_len(regex, string):
    if not regex:
        return True
    elif not string:
        return False
    elif not compare_each(regex.popleft(), string.popleft()):
        return False
    return compare_equal_len(regex, string)


args = input().split("|")
regex_in = deque(args[0])
string_in = deque(args[1])
print(compare_equal_len(regex_in, string_in))
