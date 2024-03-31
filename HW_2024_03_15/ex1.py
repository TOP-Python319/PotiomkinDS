email = input()
at_sym = email.find('@')
dot_sym = email.find('.')
if at_sym != -1 and dot_sym != -1 and at_sym < dot_sym:
    print('Да')
else:
    print('Нет')

#######################
    
# sgd@ya.ru
# Да
# abcde@fghij
# Нет