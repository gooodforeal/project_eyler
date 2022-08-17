# Простые делители числа 13195 - это 5, 7, 13 и 29.
# Каков самый большой делитель числа 600851475143, являющийся простым числом?


def is_simple(number):
    if number == 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def max_del(number):
    maxdel = 0
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0 and is_simple(i):
            maxdel = i
    return maxdel


try:
    assert max_del(13195) == 29
    assert max_del(600851475143) == 6857
except:
    print("Test error")
else:
    print("Tests passed")