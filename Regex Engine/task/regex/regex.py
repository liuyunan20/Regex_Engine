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


def compare_equal_len(regex, string):
    if not regex:
        return True
    elif not string:
        return False
    elif not compare_each(regex.popleft(), string.popleft()):
        return False
    return compare_equal_len(regex, string)


def compare_dif_len(regex, string):
    if len(regex) == len(string):
        return compare_equal_len(deque(regex), deque(string))
    elif len(regex) < len(string):
        for i in range(len(string) - len(regex) + 1):
            if compare_equal_len(deque(regex), deque(string[i: i + len(regex) + 1])):
                return True
    return False


args = input().split("|")
regex_in = list(args[0])
string_in = list(args[1])
print(compare_dif_len(regex_in, string_in))
