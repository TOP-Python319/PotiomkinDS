a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

if a % b == 0:
    print (f'{a} делится на {b} нацело', f'частное: {a // b}', sep='\n') 
elif a % b != 0:
    print (f'{a} не делится на {b} нацело', f'неполное частное: {a // b}', f'остаток: {a % b}', sep='\n')

# Введите первое число: 36
# Введите второе число: 4
# 36 делится на 4 нацело
# частное: 9
    
    
# 95 не делится на 11 нацело
# неполное частное: 8
# остаток: 7
    
# комментарий преподавателя:
# всё чисто, вопросов нет. =)