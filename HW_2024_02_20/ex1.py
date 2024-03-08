multiple_of_seven = []
n = int(input('n = '))
while n % 7 == 0:
    multiple_of_seven += [str(n)]
    n = int(input('n = '))
else: 
    print(' '.join(multiple_of_seven[::-1]))
    # формально правильно, мы получили строку содержащую ответ, но можно было сделать проще и быстрее
    # print(*multiple_of_seven[::-1], sep=' ')

####################
# n = 7
# n = 7
# n = 14
# n = 21
# n = 13
# 21 14 7 7
    

#####
# Комментарий преподавателя:

# Смотрите print(), я его упростил.
