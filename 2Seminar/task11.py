# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

n = int(input("Введите число: "))
first_fib = 0
second_fib = 1
i = 2 # Первые два числа уже известны
while second_fib < n:
    next_fib = first_fib + second_fib
    # 0 + 1 = 1
    # 1 + 1 = 2
    first_fib = second_fib
    second_fib = next_fib
    i += 1
    if second_fib > n:
        i = -1
print(i)
