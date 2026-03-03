import random

def fast_pow(x, n):
    res = 1
    while n > 0:
        if n & 1:
            res *= x
        x *= x
        n >>= 1
    return res

#ТЕСТ

def test_fast_pow():
    for _ in range(1000):
        x = random.randint(1, 10)
        n = random.randint(0, 20)
        assert fast_pow(x, n) == x ** n
    print("fast_pow: OK")

test_fast_pow()
