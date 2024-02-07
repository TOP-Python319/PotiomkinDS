whole = int(input('Введите целую часть (миль): '))
part = int(input('Введите дробную часть (миль): '))
num  = float(f'{whole}.{part}')
kilometers = num * 1.61

print (f'{whole}.{part} миль = {kilometers:.1f} км')
# Введите целую часть (миль): 7
# Введите дробную часть (миль): 513
# 7.513 миль = 12.1 км