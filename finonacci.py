def recursive(n):
    if(n==1 or n==2):
        return 1
    else:
        return recursive(n-1) + recursive(n-2)

#print(recursive(int(input(('Enter nth of terms')))))

def non_recursive(n):
    a=1
    b=1
    x=0
    for c in range(n):
        print(a,b)
        a = a+b
        b= a +b
non_recursive(int(input(('Enter nth of terms'))))