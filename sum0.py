def sum0(a):
    a = sorted(a)
    b=[]
    for x in range(len(a)-1):
        if(a[x]!=a[x+1]):
            if(a[x]+a[x+1]==0):
                b.append([a[x],a[x+1]])
    return b
                