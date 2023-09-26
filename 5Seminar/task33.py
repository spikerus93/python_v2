# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

new_list = [i for i in range(5)]
print(new_list)
new_list.clear()  # new_list = []
for i in range(5):
    new_list.append(i)
print(new_list)
n = int(input("Input count marks: "))
marks = [int(i) for i in input("Input marks: ").split()[:n]]
print([min(marks) if i == max(marks) else i for i in marks])