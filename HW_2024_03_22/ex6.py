dict_of_letters = {}
j = 97
for i in range(10, 36):
    letter = chr(j)
    d = {i: letter}
    dict_of_letters.update(d)
    j += 1

def dec_to_free(dec_num: int, base:int):
    if not(2 <= base <= 36):
        return None
    
    new_num = ''
    while dec_num > 0:
        remainder = dec_num % base
        if remainder < 10:
            new_num = str(remainder) + new_num
        elif remainder in dict_of_letters:
            new_num = dict_of_letters[remainder] + new_num
        dec_num //= base
    return new_num


def int_base(number: str, from_base: int, to_base: int):
    if not(2 <= to_base <= 36):
        return None
    
    free_num = dec_to_free(int(number, from_base), to_base)
    return free_num


print(int_base('ff00', 16, 2))
print(int_base('1101010', 2, 30))
print(int_base('1554982', 10, 30))

##################################

# 1111111100000000
# 3g
# 1rhmm