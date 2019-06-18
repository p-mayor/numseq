def fib(x):
    '''return the xth number in the fibonacci sequence'''
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
            fin = a + b
            a = b
            b = fin
    return fin
