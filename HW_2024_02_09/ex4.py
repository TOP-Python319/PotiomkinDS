coord1 = input('Введите координаты первой клетки: ')
coord2 = input('Введите координаты второй клетки: ')

if (((ord(coord1[0]) + int(coord1[1])) % 2 == 0 and (ord(coord2[0]) + int(coord2[1])) % 2 == 0) 
    or ((ord(coord1[0]) + int(coord1[1])) % 2 == 1 and (ord(coord2[0]) + int(coord2[1])) % 2 == 1)):
    print ('да')
else: 
    print ('нет')

# Введите координаты первой клетки: a1
# Введите координаты второй клетки: b2
# да

# Введите координаты первой клетки: f5
# Введите координаты второй клетки: a5
# нет

# можно добавить ещё переменных, чтобы код выглядел более осмысленным
# условие сразу читается гораздо легче

# first_letter = ord(coord1[0])
# first_digit = int(coord1[1])
# second_letter = ord(coord2[0])
# second_digit = int(coord2[1])

# if (((first_letter + first_digit) % 2 == 0 and (second_letter + second_digit) % 2 == 0) 
#     or ((first_letter + first_digit) % 2 == 1 and (second_letter + second_digit) % 2 == 1)):
#     print ('да')
# else: 
#     print ('нет')