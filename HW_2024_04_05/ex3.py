with open('nums.txt', 'r', encoding='utf-8') as file:
    text = file.readlines()
    res = 0
    for part in text:
        num = ''.join(sym if sym.isdigit() else ' ' for sym in part).split()
        for n in num:
              res += int(n)
    print(res) 

##############################################

# 124410