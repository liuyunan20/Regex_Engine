args = input().split("|")


def compare(regex, string):
    if not regex:
        return True
    elif not string:
        return False
    elif regex == ".":
        return True
    elif regex == string:
        return True
    return False


print(compare(*args))

