coord1 = input('Введите координаты первой клетки: ')
coord2 = input('Введите координаты второй клетки: ')

symbol1 = ord(coord1[0])
symbol2 = int(coord1[1])
symbol3 = ord(coord2[0])
symbol4 = int(coord2[1])
a = symbol1 + symbol2
b = symbol3 + symbol4

if ((b - 2) <= a <= (b + 2)):
    print ('да')
else:
    print ('нет')

# Введите координаты первой клетки: e6
# Введите координаты второй клетки: d5
# да

# Введите координаты первой клетки: c4
# Введите координаты второй клетки: d6
# нет