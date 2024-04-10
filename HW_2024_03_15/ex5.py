word = input('Введите слово: ')
score_count = 0
    
scores_letters = {
    1: 'АВЕЁИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}

for letter in word:
    for key, value in scores_letters.items():
        if letter.upper() in value:
            score_count += key

print(score_count)

#############################################

# Введите слово: синхрофазатрон
# 29

# комментарий преподавателя
# всё верно!
