def square(n):
    '''return n squared'''
    return n*n


def triangle(n):
    '''return nth triangle num'''
    output = 0
    for i in range(0, n):
        output += i+1
    return output


def cube(n):
    '''return n cubed'''
    return n*n*n
