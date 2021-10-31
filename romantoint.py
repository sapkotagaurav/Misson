
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
    
print(romantoint(input("Enter:\t").upper()))