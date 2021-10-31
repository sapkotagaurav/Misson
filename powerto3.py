def threepower(num):
    for a in range(100):
        if(num==1):
            return(0,0)
        if(num<=3**(a+1) and num>3**a):
            print(num-3**(a+1))
            return (num - 3**a,a)
        
            
    
def secfun(num):
    a = num
    b=[]
    while(a>=1):
        x =threepower(a)
        a =x[0]
        b.append(x[1])
    return(b)
        
        
def isPower(arr):
    for a in range(len(arr)-1):
        for b in range(a+1,len(arr)):
            if(arr[a]==arr[b]):
                return False
    return True
        
print(secfun(27))
        