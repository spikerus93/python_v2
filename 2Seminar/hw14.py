# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

N = int(input("Введите число N: "))
i = 1
while i <= N:  
    if N % 2 != 0:
        print("Это не целое число!")
        break
    else:
        print(f"Все целые степени двойки - {i}")
        i = i * 2
