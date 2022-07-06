
d ={
    "I":1,
    "X":10,
    "V":5,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}

def romantoint(s):
    a = 0
    for ab in range(len(s)):
        try:
            if(s[ab]=="I" and (s[ab+1]=="V" or s[ab+1]=="X")):
                a-=1
            elif(s[ab]=="X" and (s[ab+1]=="C" or s[ab+1]=="L")):
                a-=10
            elif(s[ab]=="C" and (s[ab+1]=="D" or s[ab+1]=="M")):
                a-=100
            else:
                a+=d[s[ab]]
        except IndexError:
            a+=d[s[ab]]
            
            
        
    return a
    
#print(romantoint(input("Enter:\t").upper()))


def int_to_roman(x):
    values = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    res=""
    for i in values:
        res+=(x//i) *values[i]
        x %=i
    return res

print(int_to_roman(1994))