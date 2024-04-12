# def countable_nouns(number: int, plural_forms: tuple[str, str, str], ) -> str:
#     if number % 10 in (0, 5, 6, 7, 8, 9) or num in range(10, 21):
#     # if str(number)[-1] in '056789' or str(number)[:2] in ['10', '11',...'20']:
#         return plural_forms[2]
#     elif number % 10 == 1:
#         return plural_forms[0]
#     else:
#         return plural_forms[1]

# print(countable_nouns(1, ("год", "года", "лет")))  

def countable_nouns(number: int, plural_forms: tuple[str, str, str], ) -> str:
    if number % 10 == 1 and (number % 100 != 11):
        return plural_forms[0]
    elif number % 10 in [2, 3, 4] and (number % 100 not in [12, 13, 14]):
        return plural_forms[1]
    else:
        return plural_forms[2]   
    
print(countable_nouns(1, ("год", "года", "лет")))
print(countable_nouns(2, ("год", "года", "лет")))
print(countable_nouns(10, ("год", "года", "лет")))
print(countable_nouns(12, ("год", "года", "лет")))
print(countable_nouns(22, ("год", "года", "лет")))
print(countable_nouns(111, ("год", "года", "лет")))
print(countable_nouns(10319, ("год", "года", "лет")))
print(countable_nouns(100001, ("год", "года", "лет")))