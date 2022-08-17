# Число-палиндром с обеих сторон (справа налево и слева направо) читается
# одинаково. Самое большое число-палиндром, полученное умножением двух
# двузначных чисел – 9009 = 91 × 99.
# Найдите самый большой палиндром, полученный умножением
# двух трехзначных чисел.


def is_palindrome(number):
    number = str(number)
    if len(number) < 1:
        return True
    if number[0] == number[-1]:
        return is_palindrome(number[1:-1])
    return False


def max_palindrome():
    max_palindrome = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            if is_palindrome(i * j):
                max_palindrome = i * j
    return max_palindrome


try:
    assert max_palindrome() == 580085
except:
    print("Test error")
else:
    print("Tests passed")