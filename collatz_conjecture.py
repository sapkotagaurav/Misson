from random import randrange
import matplotlib.pyplot as plt
from sympy import true

x=[]

def collatz_conjucture(n):
    x.append(n)
    if n==1:
        return n
    if n%2==0:
        return collatz_conjucture(n/2)
    else:
        return collatz_conjucture((3*n+1)/2)
    
for  a in range(10):
    collatz_conjucture(randrange(1,450))
    plt.plot(x,linestyle="solid",scalex=True)
    x=[]
     
collatz_conjucture(1222)
print(x)

plt.show()