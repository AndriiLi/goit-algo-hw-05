# Homework 5

## Environment
used python version Python 3.12.1


## Task 1
Реалізуйте функцію caching_fibonacci, яка створює та використовує кеш для зберігання і повторного використання вже обчислених значень чисел Фібоначчі.

```
fib = caching_fibonacci()

print(fib(10))  # Виведе 55
```


## Task 2

Необхідно створити функцію generator_numbers, яка буде аналізувати текст, ідентифікувати всі дійсні числа, що вважаються частинами доходів, і повертати їх як генератор.

```
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід,
        доповнений додатковими надходженнями 27.45 і 324.00 доларів."
        
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

Загальний дохід: 1351.46
```

## Task 3

Розробіть Python-скрипт для аналізу файлів логів. Скрипт повинен вміти читати лог-файл, 
переданий як аргумент командного рядка, і виводити статистику за рівнями логування 
наприклад, INFO, ERROR, DEBUG.

> Supported parameters
- sort - sort line log presentation by date (asc | desc)
- limit - limit output log presentation

```
 python hw_05_3.py ./src/logfile.txt
 python hw_05_3.py ./src/logfile.txt info
 ```
> extra options
```
 python hw_05_3.py ./src/logfile.txt info asc
 python hw_05_3.py ./src/logfile.txt info desc  
 python hw_05_3.py ./src/logfile.txt info asc 5
```


## Task 4

Доробіть консольного бота помічника з попереднього домашнього завдання та додайте обробку помилок за допомоги декораторів.