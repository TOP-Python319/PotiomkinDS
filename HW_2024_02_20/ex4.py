n = int(input('n = '))
var = '9' * n
num_1 = int('1' + '0' * (n-1))
num_2 = int(var)
counter = 0
for i in range(num_1, num_2):
    counter_j = 0
    for j in range(2, i // 2 + 1):
        if (i % j == 0):
            counter_j += 1
    if (counter_j == 0):
            counter += 1

print(f'среди всех {n}-значных чисел {counter} - простых')

#####################

# n = 3
# среди всех 3-значных чисел 143 - простых