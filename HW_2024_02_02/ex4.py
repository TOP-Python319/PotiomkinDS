num = int(input('Введите трехзначное число: '))
digit_3 = num % 10
digit_2 = num // 10 % 10
digit_1 = num // 100


print(f'сумма цифр числа {num} = {(digit_1 + digit_2 + digit_3)}\nпроизведение ицфр = {(digit_1 * digit_2 * digit_3)}')
# сумма цифр числа 546 = 15
# произведение ицфр = 120