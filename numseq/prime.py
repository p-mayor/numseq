import math
# ref: https://stackoverflow.com/questions/11619942/print-series-of-prime-numbers-in-python


def primes(n):
    primes = [2]
    for num in range(3, n, 2):
        if all(num % i != 0 for i in range(2, int(math.sqrt(num))+1)):
            primes.append(num)
    return primes


def is_prime(m):
    if m in primes(m+1):
        return True
    else:
        return False
