list_of_dicts = [
    {
        'Барнаул': 7,
        'Владивосток': 9,
        'Волгоград': 9,
        'Ижевск': 5,
        'Махачкала': 7,
        'Москва': 9,
        'Омск': 9,
        'Саратов': 4,
        'Ульяновск': 3
    },
    {
        'Казань': 8,
        'Краснодар': 2,
        'Москва': 3,
        'Самара': 3,
        'Санкт-Петербург': 6,
        'Тюмень': 1,
        'Уфа': 7
    },
    {
        'Ижевск': 1,
        'Иркутск': 3,
        'Кемерово': 1,
        'Москва': 3,
        'Саратов': 3,
        'Хабаровск': 6
    },
    {
        'Барнаул': 7,
        'Оренбург': 3,
        'Санкт-Петербург': 1,
        'Тюмень': 4,
        'Ярославль': 3
    }
]


from collections import defaultdict

new_dict = defaultdict(set)

for dicts in list_of_dicts:

#     for key in dicts:
#         if key not in str(new_dict):
#             new_dict.update({key: dicts[key]})
        # elif key in str(new_dict):
        #     new_dict.update({key: (new_dict[key], dicts[key])})

# print(*new_dict, sep='\n')
            
    for key, value in dicts.items():
        new_dict[key].add(value)

for key, value in new_dict.items():
    print(f'{key}: {value}')

#############################################
    
# в строках 46-52 мои попытки сделать самостоятельно, но они не совсем 
# правильные. Оставлю это здесь, вдруг когда-нибудь пригодится подсмотреть

##############################################
    
# вывод правильного(рабочего) варианта
# Барнаул: {7}
# Владивосток: {9}
# Волгоград: {9}
# Ижевск: {1, 5}
# Махачкала: {7}
# Москва: {9, 3}
# Омск: {9}
# Саратов: {3, 4}
# Ульяновск: {3}
# Казань: {8}
# Краснодар: {2}
# Самара: {3}
# Санкт-Петербург: {1, 6}
# Тюмень: {1, 4}
# Уфа: {7}
# Иркутск: {3}
# Кемерово: {1}
# Хабаровск: {6}
# Оренбург: {3}
# Ярославль: {3}