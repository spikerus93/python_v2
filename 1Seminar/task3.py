# Задача №3. Общее обсуждение
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

a = int(input('Введите количество учеников в первом классе:'))
b = int(input('Введите количество учеников во втором классе:'))
c = int(input('Введите количество учеников в третьем классе:'))
sum1 = a//2 + a % 2
sum2 = b//2 + b % 2
sum3 = c//2 + c % 2
print(sum1 + sum2 + sum3)

