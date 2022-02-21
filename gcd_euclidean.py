def gcd(x,y):
    
    
    if x>y:
        x,y==y,x
    
    r= y%x
    divisor =x
    while r>0:
        r=y%divisor
        if r==0:break
        y=divisor
        divisor =r
    return divisor

def lcm(a,b):
    return a*b//gcd(a,b)
print(gcd(int(input("Enter first number:")),int(input("Enter second number:"))))
        
        

            
            