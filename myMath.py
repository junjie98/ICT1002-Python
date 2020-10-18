def add(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def evenNum(x):
    enum = []
    for num in x:
        if num % 2 == 0:
            enum.append(num)
    return enum


def maximum(x):
    return max(x)


def minimum(x):
    return min(x)


def absolute(x):
    return abs(x)


def sumTotal(x):
    return sum(x)


def clear(x):
    clear = []
    for i in x:
        if i > 0:
            clear.append(0)
        else:
            pass
    return clear
