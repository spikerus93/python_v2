# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2

n = int(input("Введите количество монеток: "))
x1 = 0  # Монетка лежит Орлом вверх
x2 = 0  # Монетка лежит Решкой вверх

for i in range(n):
    print(f'{x1} = Орел')
    print(f'{x2} = Решка')
    x = int(input("Введите как лежат монетки, где 0=Орлом, 1=Решкой: "))
    if x == 0:
        x1 += 1
    elif x == 1:
        x2 += 1       

if x1 < x2:
    print(f'Надо перевернуть {x1} монеток')
else:
    print(f'Надо перевернуть {x2} монеток')

# Доп. решение.
# Task 10
# n = int(input("Введите кол-во монет: "))
# count_zero = 0
# count_one = 0
# for i in range(n):
#     x = int(input("Введите сторону монеты(1 или 0): "))
#     if x == 1:
#         count_one += 1
#     else:
#         count_zero += 1
# if count_zero > count_one:
#     print(count_one)
# else:
#     print(count_zero)