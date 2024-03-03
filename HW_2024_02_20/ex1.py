multiple_of_seven = []
n = int(input('n = '))
while n % 7 == 0:
    multiple_of_seven += [str(n)]
    n = int(input('n = '))
else: 
    print(' '.join(multiple_of_seven[::-1]))

####################
# n = 7
# n = 7
# n = 14
# n = 21
# n = 13
# 21 14 7 7