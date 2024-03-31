
fruits = []
fruit = input()
while fruit != '':
    fruits.append(fruit)
    fruit = input() 
if len(fruits) == 1:
        print(''.join(fruits))
else:
        fruits.insert(-1, 'и')
        fru = (', '.join(fruits)).replace(', и,', ' и')
        print(fru)    

###########################################

# яблоко

# яблоко

# яблоко
# груша

# яблоко и груша

# яблоко
# груша
# апельсин

# яблоко, груша и апельсин
        
# яблоко 
# груша
# апельсин
# лимон

# яблоко, груша, апельсин и лимон