'''   
    aabbbcdda -> a2b3c1d2a1
    '''

def f(s:str):
    s=s.lower()
    i,j=0,0
    cha=s[0]
    a=""
    while i<len(s):
        if s[i] != cha:
            if j!=1:
                a =a + cha + str(j)
            else:
                a =a +cha
            cha = s[i]
            j=0


        j+=1
        i+=1
            
    return a

print(f("aabccd"))