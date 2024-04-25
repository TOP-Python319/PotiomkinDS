def create_counter():
    counter = 0

    def increment(value = 1):
        nonlocal counter
        counter += value
        return counter
   
    def decrement(value = 1):
        nonlocal counter
        counter -= value
        return counter
    
    return increment, decrement


inc_1, dec_1 = create_counter()

print(inc_1())
print(inc_1(2))
print(inc_1(3))
print(dec_1())
print(dec_1())

###########################################

# 1
# 3
# 6
# 5
# 4




inc_2, dec_2 = create_counter()

print(inc_2(10))
print(dec_2(5))
print(inc_2(100))
print(inc_2(50))
print(dec_2())

###########################################

# 10
# 5
# 105
# 155
# 154