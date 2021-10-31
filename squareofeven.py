'''A function to find square of even positioned digits 
example 1234678 will return 2^2 +4^2 +7^2
'''

def rev_num(num):
    n2=0
    while(num>0):
        n2 = n2*10 +(num%10)
        num = int(num/10)
    return n2

def sqeven(num):
    n2 = rev_num(num)
    n = 0
    x =0
    while(n2>0):
        n +=1
        if (n%2==0):
            x = x + (n2%10)**2
        n2=int(n2/10)
    return x

print(sqeven(123456))  
            
        
    