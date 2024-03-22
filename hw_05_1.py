from typing import Callable


def caching_fibonacci() -> Callable[[int], int]:
    cache = {}

    def fibonacci(value: int) -> int:
        if value <= 0:
            return 0
        if value == 1:
            return 1
        if value in cache:
            return cache[value]

        cache[value] = fibonacci(value - 1) + fibonacci(value - 2)
        return cache[value]

    return fibonacci


if __name__ == '__main__':
    fib = caching_fibonacci()

    print(f"fibonacci for 10: {fib(10)}")  # Виведе 55
    print(f"fibonacci for 15: {fib(15)}")  # Виведе 610
