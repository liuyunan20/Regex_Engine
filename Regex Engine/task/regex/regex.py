from collections import deque
import sys
sys.setrecursionlimit(10000)


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


def compare_equal_len(regex: list, string: list) -> bool:
    global flag
    if not regex:
        return True
    if not string:
        return False
    if regex[0] == "\\":
        if regex[1] == "." and string[0] == ".":
            string.pop(0)
            regex.pop(0)
            regex.pop(0)
            return compare_equal_len(regex, string)
        elif regex[1] == "." and string[0] != ".":
            return False
        elif compare_each(regex[1], string[0]):
            regex.pop(0)
            regex.pop(0)
            string.pop(0)
            return compare_equal_len(regex, string)
        else:
            return False
    elif not compare_each(regex[0], string[0]):
        if regex[0] == "?":
            regex.pop(0)
            return compare_equal_len(regex, string)
        if len(regex) >= 2 and (regex[1] == "?" or regex[1] == "*" or (flag == 1 and regex[1] == "+")):
            regex.pop(0)
            regex.pop(0)
            flag = 0
            return compare_equal_len(regex, string)
        return False
    elif len(regex) >= 2 and (regex[1] == "*" or regex[1] == "+"):
        string.pop(0)
        flag = 1
        if not string:
            return True
        if len(regex) > 2 and len(string) == len(regex) - 2:
            regex.pop(0)
            regex.pop(0)
        return compare_equal_len(regex, string)

    string.pop(0)
    regex.pop(0)
    return compare_equal_len(regex, string)


def compare_dif_len(regex: list, string: list) -> bool:
    if not regex:
        return True
    if regex[0] == "^" and regex[-1] == "$":
        compare_equal_len(regex[1: len(regex) - 1], string)
        if not string:
            return True
        return False
    if regex[0] == "^":
        return compare_equal_len(regex[1:], string)
    if regex[-1] == "$":
        regex.pop()
        while string:
            string_colon = [x for x in string]
            regex_colon = [x for x in regex]
            if compare_equal_len(regex_colon, string_colon) and not string_colon:
                return True
            string.pop(0)
        return False
    while string:
        string_colon = [x for x in string]
        regex_colon = [x for x in regex]
        if compare_equal_len(regex_colon, string_colon):
            return True
        string.pop(0)
    return False


flag = 0
args = input().split("|")
regex_in = list(args[0])
string_in = list(args[1])
print(compare_dif_len(regex_in, string_in))
