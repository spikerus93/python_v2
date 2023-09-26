# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: Вывод:
# 1 2 3 2 3 2

numbers = [int(i) for i in input("Введите числа: ").split()]

count_numbers = {}

for i in numbers:
    if i not in count_numbers: #count_numbers.keys()
        count_numbers[i] = 1 # 1 - потому что одно число ужен на встретилось
    else:   # i является ключом словаря
        count_numbers[i] += 1
print(count_numbers)
print(sum([i//2 for i in count_numbers.values()]))

        