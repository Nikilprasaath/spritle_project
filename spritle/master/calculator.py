def zero(cal=None):
    if cal is None:
        return 0
    else:
        return cal(0)

def one(cal=None):
    if cal is None:
        return 1
    else:
        return cal(1)

def two(cal=None):
    if cal is None:
        return 2
    else:
        return cal(2)

def three(cal=None):
    if cal is None:
        return 3
    else:
        return cal(3)

def four(cal=None):
    if cal is None:
        return 4
    else:
        return cal(4)

def five(cal=None):
    if cal is None:
        return 5
    else:
        return cal(5)

def six(cal=None):
    if cal is None:
        return 6
    else:
        return cal(6)

def seven(cal=None):
    if cal is None:
        return 7
    else:
        return cal(7)

def eight(cal=None):
    if cal is None:
        return 8
    else:
        return cal(8)

def nine(cal=None):
    if cal is None:
        return 9
    else:
        return cal(9)

def plus(num2):
    return lambda num1: num1 + num2

def minus(num2):
    def func(num1):
        out = num1 - num2
        return out
    return func

def times(num2):
    return lambda num1: num1 * num2

def divided_by(num2):
    return lambda num1: num1 // num2

