def orth_triangle(*, cath1: float=0, cath2: float=0, hyp: float=0) -> float | None:
    if cath1 < 0 and cath2 < 0 and hyp  < 0:
        return None
    
    if cath1 != 0 and cath2 != 0 and hyp != 0:
        return None

    if hyp == 0:
        return(cath1**2 + cath2**2) ** 0.5
    
    cat_sum = cath1 + cath2

    if hyp > cat_sum:
        return (hyp ** 2 - cat_sum ** 2) ** 0.5
    else:
        return None


print(orth_triangle(cath1=3, hyp=5))
print(orth_triangle(cath1=8, cath2=15))
print(orth_triangle(cath2=9, hyp=3))