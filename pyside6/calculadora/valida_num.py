def isNumOrDot(string):
    if string in ('0123456789.'):
        return True
    return False


def isEmpty(string: str):
    return len(string) == 0


def isNumber(string: str):
    try:
        float(string)
        valid = True
    except ValueError:
        valid = False
    return valid
