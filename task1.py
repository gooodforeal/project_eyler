# Если выписать все натуральные числа меньше 10, кратные 3 или 5,
# то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
# Найдите сумму всех чисел меньше 1000, кратных 3 или 5.


def get_sum(num_count):
    current_sum = 0
    for i in range(num_count):
        if i % 3 == 0 or i % 5 == 0:
            current_sum += i
    return current_sum


try:
    assert get_sum(1000) == 233168
    assert get_sum(10) == 23
except:
    print("Test error")
else:
    print("Tests passed")


