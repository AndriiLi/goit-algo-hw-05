import re
from decimal import Decimal, getcontext, ROUND_HALF_EVEN
from typing import Iterator, Callable

getcontext().prec = 8


def generator_numbers(string: str) -> Iterator[Decimal]:
    digits = re.findall(r"-?\d+\.?\d*", string)
    for digit in digits:
        yield Decimal(digit)


def sum_profit(string: str, generator_of_numbers: Callable[[str], Iterator[Decimal]]) -> Decimal:
    result = Decimal('0')

    for i in generator_of_numbers(string):
        result += Decimal(i)

    return result.quantize(Decimal('0.00'), rounding=ROUND_HALF_EVEN)


if __name__ == '__main__':
    text = """Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід,
              доповнений додатковими надходженнями 27.45 і 324.00 доларів"""

    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")  # Загальний дохід: 1351.46
