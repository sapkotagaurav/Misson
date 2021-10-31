def rev_num(num):
    n2=0
    while(num>0):
        n2 = n2*10 +(num%10)
        num = int(num/10)
    return n2

def dectobinary(num):
    binary =""
    while(num>0):
        binary +="{}".format(num%2)
        num = num//2
    return rev_num(int(binary))

print(dectobinary(241))

def binary_to_decimal(num):
    x=0
    count =0
    while(num>0):
        x = x+(num%10)*2**(count)
        num = num//10
        count+=1
    return x

print(binary_to_decimal(11110001))