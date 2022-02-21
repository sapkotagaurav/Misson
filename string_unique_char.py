'''A program to test if the string has all unique characters'''
#first approach
def f(s:str):
    for a in range(len(s)):
        for b in range(a+1,len(s)-1):
            if s[a] == s[b]:
                return False
    return True

#print(f(input("s:")))

#brute_force

def f2(s:str):
    for a in range(len(s)):
        if s[a] in s[a+1:]:
            return False
    return True

#print(f2(input("s:")))

#using dictionary
def f3(s:str):
    d={}
    for a in s:
        if d.get(a,None):
            return False
        else:
            d[a]=d.get(a,0)+1
    return True
print(f3(input("s:")))