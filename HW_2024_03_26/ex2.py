def flatten(l: list) -> list:
    if not isinstance(l, list) and not isinstance(l, tuple): 
        return[l]
    elif len(l) == 1:
        return flatten(l[0])
    else:
        return flatten (l[0]) + flatten(l[1:])
    

print(flatten([1, [2, 3, [4]], 5]))
print(flatten([1, [2, 3], [[2], 5], 6]))
print(flatten([[[[9]]], [1, 2], [[8]]]))

#############################

# [1, 2, 3, 4, 5]
# [1, 2, 3, 2, 5, 6]
# [9, 1, 2, 8]