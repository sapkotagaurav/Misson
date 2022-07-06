

def add_binary(s1,s2):
    carry=0
    sum=""
    lon = s1 if len(s1)>len(s2) else s2
    shor = s1 if lon ==s2 else s2
    shor ="0"* (len(lon)-len(shor)) + shor
    for a in range(len(lon)-1,-1,-1):
        if carry:
            if lon[a]==shor[a]=="1":
                carry=1
                sum+="1"
            elif lon[a]==shor[a]=="0":
                carry=0
                sum+="1"
            else:
                carry = 1
                sum+="0"
        else:
            if lon[a]==shor[a]=="1":
                carry=1
                sum+="0"
            elif lon[a]==shor[a]=="0":
                carry=0
                sum+="0"
            else:
                carry = 0
                sum+="1"
    if carry: sum+="1"
    return sum[::-1]


print(add_binary("1011","1010"))
