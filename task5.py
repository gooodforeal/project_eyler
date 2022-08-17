# 2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
# Какое самое маленькое число делится нацело на все числа от 1 до 20?


from itertools import count


def get_min_del():
    i = 1
    while True:
        print(i)
        count = 0
        for d in range(1, 21):
            if i % d == 0:
                count += 1
            else:
                break
        if count == 20:
            return i
        i += 1



print(get_min_del())