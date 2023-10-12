# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
# Передать работу посредством PullRequest

import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()

uniq_values = data['whoAmI'].unique()  # Получаем уникальные значения
one_hot = pd.DataFrame()  # Создаем новый Датафрейм

# Поиск уникальных значений для добавления в новый Датафрейм с столбцом Значения.
for value in uniq_values:
    one_hot[value] = (data['whoAmI'] == value).astype(int)
one_hot.head()
print(one_hot)
