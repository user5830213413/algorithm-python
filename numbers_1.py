num = 5689 # четрых значное число, если четерых значное то возводим в степень 3
first_digit = num // 10 ** 3 # первая цифра
test_1 = (num // 10 ** 2) % 10 # вторая цифра
test_2 = (num // 10) % 10 # предпоследняя
test_3 = num % 10 # последняя
print(f'{first_digit}\n{test_1}\n{test_2}\n{test_3}')

# разложение на множетили, x = целое число
def simple(x):
    divisor = 2
    test = []
    while x > 1:
        if x % divisor == 0:
            test.append(divisor)
            x //= divisor
        else:
            divisor += 1
    return test
print(simple(56))