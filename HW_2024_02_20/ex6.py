ticket = input('цифры билета: ')
sum_1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
sum_2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
if (sum_1 == sum_2):
    print('Билет - счастливый')
else: 
    print('Билет - не счастливый')

####################

# цифры билета: 183534
# Билет - счастливый

# цифры билета: 401367
# Билет - не счастливый