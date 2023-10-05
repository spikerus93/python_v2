# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод: Вывод:
# пара-ра-рам рам-пам-папам па-ра-па-дам Парам пам-пам

stroka = input("Введите кричалки Винни-Пуха")

def rhytm(words):
    return sum(1 for i in words if i in 'аеёиоуыэюя')
  
phrase = stroka.lower().split()
if len(phrase) <= 1:
    print("Количество фраз должно быть больше одной!")
else:
    count = rhytm(phrase[0])
    if all([rhytm(i) == count for i in phrase]):
        print('Парам пам-пам')
    else:
        print('Пам парам')


