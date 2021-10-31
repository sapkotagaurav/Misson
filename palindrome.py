def string_palindrome(string):
    string2 = ""
    for a in string:
        string2+=a
    return True if(string2==string) else  False


def rev_num(num):
    n2=0
    num2 = num *-1 if(num<0) else num
    num3=num2
    while(num2>0):
        n2 = n2*10 +(num2%10)
        num2 = int(num2/10)
    return n2 if(num3==num) else n2*-1
        

print(rev_num(-321))


def num_palindrome(num:int)-> bool:
    num2 = 0
    n= num
    while(n>0):
        lastDigit = int(n%10)
        num2 = int(num2 *10 + lastDigit)
        n=int(n/10)
    return True if(num == num2) else False

def armstrong(num):
    n=num
    n1 = 0
    while(n>0):
        n1 += (n%10) **3
        n = int(n/10)
    return True if(num==n1) else False

def arm_till_n(n):
    li = []
    for a in range(n):
        if(armstrong(a)):
            li.append(a)
    return li


print(arm_till_n(1053))
        