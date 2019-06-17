def add(a, b):
    return a + b


def fib(x):
    a = 0
    b = 1
    fin = 0

    if x == 0:
        fin = "input value must be greater than 0"
    elif x == 1:
        fin = 0
    elif x == 2:
        fin = 1
    else:
        for i in range(2, x):
            fin = add(a, b)
            a = b
            b = fin
    return fin
