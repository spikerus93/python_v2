# Задача №25. Общее обсуждение
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

str1 = 'a a a b c a a d c d d'.split()
print(str1)
my_dict = {}

for i in str1:
    if i not in my_dict:
        my_dict[i] = 1
        print(i, end= ' ')
    else:
        print(f'{i}_{my_dict[i]}', end= ' ')
        my_dict[i] += 1
        
