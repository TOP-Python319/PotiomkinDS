num = int(input('Введите натуральное число n: '))
row = [1, 1]
for i in range(1, num -1):
    row.append(row[-1] + row[-2])
print(*row)

#########################

# Введите натуральное число n: 17
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597

#####
# Комментарий преподавателя:
# Всё верно!