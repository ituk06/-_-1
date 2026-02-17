import random


def mul_bits(x, y, bits):
    x &= (2 ** bits - 1)
    y &= (2 ** bits - 1)
    return x * y


def mul16(x, y):

    a = x >> 8
    b = x & 0xFF
    c = y >> 8
    d = y & 0xFF

    ac = mul_bits(a, c, 8)
    ad = mul_bits(a, d, 8)
    bc = mul_bits(b, c, 8)
    bd = mul_bits(b, d, 8)

    result = (ac << 16) + ((ad + bc) << 8) + bd
    return result


def test_mul16():
    for _ in range(10000):
        x = random.randint(0, 65535)
        y = random.randint(0, 65535)
        assert mul16(x, y) == x * y, f"Ошибка: {x} * {y} 😥"
    print("Все тесты пройдены 🤩")


test_mul16()
