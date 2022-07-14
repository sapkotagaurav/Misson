import math

def powe(a,b):
    if b==0:
        return 1
    if b%2==0:
        x = powe(a,b/2)
        return x*x
    else:
        return a*powe(a,b-1) if b>0 else (1/a)*powe(a,b+1)


print(powe(2,-2))