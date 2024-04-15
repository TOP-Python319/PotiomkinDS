def double_fact(n: int) -> int:
    if n < 0:
        return None
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * double_fact(n - 2)
    
print(double_fact(6))
print(double_fact(5))
print(double_fact(2))
print(double_fact(4))
print(double_fact(-1))

###########################

# 48  
# 15  
# 2   
# 8   
# None