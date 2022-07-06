import math


def atoi(s):
    r=0
    p = True
    p_hit=False
    numhit=False
    dec = False
    d ={'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,"+":"+","-":"-",}

    for a in s:
        if a in d.keys():
            if a=='-' or a=="+":
                if p_hit:
                    return r if p else r*-1
                p_hit=True
                p= False if a=='-' else True
            else:
                r = r*10+d.get(a)
                if r>2147483648:
                    return 2147483648 if p else  -2147483648
        else:
            if r:
                return r if p else r*-1
            if a!=" ":
                return r if p else r*-1

    return r if p else r*-1

print(atoi("-91283472332"))


