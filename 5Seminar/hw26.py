# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

A = int(input("Введите число A: "))
B = int(input("Введите число В: "))

def product(A, B):
    if A == 0:
        return 1
    if B == 1:
        return A
    else:
        return (A ** B)
print(product(A,B))

#Доп. решение.
# def f(a, b):
#   if b == 0:
#     return 1
#   return f(a, b - 1) * a