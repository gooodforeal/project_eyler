# Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих.
# Начиная с 1 и 2, первые 10 элементов будут:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.


def fibo_sum(size):
    sum_elements = 2
    last_two = [1, 2]
    tmp = sum(last_two)
    while tmp < size:
        if tmp % 2 == 0:
            sum_elements += tmp
        last_two.append(tmp)
        last_two.pop(0)
        tmp = sum(last_two)
    return sum_elements


try:
    assert fibo_sum(90) == 44
    assert fibo_sum(4000000) == 4613732
except:
    print("Test error")
else:
    print("Tests passed")




