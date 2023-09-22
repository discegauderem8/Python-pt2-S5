import math


def get_prime_digits():
    yield 2
    primes = [2]
    current = 3

    while True:
        is_prime = True
        max_divisor = math.isqrt(current)+1

        for divisor in primes:
            if divisor > max_divisor:
                break
            if current % divisor == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(current)
            yield current

        current += 2

gen = get_prime_digits()

for _ in range(10):
    print(next(gen))

