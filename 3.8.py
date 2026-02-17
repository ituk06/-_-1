import random


def mul_bits(x, y, bits):

    x &= (2 ** bits - 1)
    y &= (2 ** bits - 1)
    return x * y


def mul16k(x, y):

    a = x >> 8
    b = x & 0xFF
    c = y >> 8
    d = y & 0xFF

    p1 = mul_bits(a, c, 8)          # a*c
    p2 = mul_bits(b, d, 8)          # b*d
    p3 = mul_bits(a + b, c + d, 9)  # (a+b)*(c+d)

    cross = p3 - p1 - p2

    result = (p1 << 16) + (cross << 8) + p2
    return result


# ТЕСТ


def test_mul16k():
    for _ in range(1000):
        x = random.randint(0, 65535)
        y = random.randint(0, 65535)
        assert mul16k(x, y) == x * y, f"Ошибка: {x} * {y}"
    print("Все тесты пройдены!")


test_mul16k()
