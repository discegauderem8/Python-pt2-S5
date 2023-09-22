def fibonacci(n):
    start_value = 1
    i = 0

    yield 1
    yield 1

    digits = [start_value, start_value]
    while (i < n):
        swap = digits[0] + digits[1]
        yield swap
        digits[0] = digits[1]
        digits[1] = swap
        i += 1


n = int(input("До какого числа вывести последовательность Фибоначчи?  "))

for i in (fibonacci(n)):
    print(i)
