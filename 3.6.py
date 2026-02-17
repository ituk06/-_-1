import random


def fast_mul_rec(x, y):

    if y == 0:
        return 0
    if y & 1:
        return x + fast_mul_rec(x << 1, y >> 1)
    else:
        return fast_mul_rec(x << 1, y >> 1)


def test_fast_mul_rec():
    for _ in range(1000):
        a = random.randint(0, 1000)
        b = random.randint(0, 1000)
        assert fast_mul_rec(a, b) == a * b, f"Ошибка: {a} * {b} 🥴"
    print("Все тесты пройдены 😻")


test_fast_mul_rec()
