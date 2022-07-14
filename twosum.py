def twosum(array,target):
    for a in range(len(array)-1):
        for b in range(a+1,len(array)):
            if(array[a]+array[b]==target):
                return [a,b]
        
print(twosum([1,2,5,4,2,8,2,9,0],6))


def two_sum(l:list,tar):
    d ={}
    for i in range(len(l)):
        print(l[i],tar-l[i],d.get(tar-l[i]))
        if d.get(tar-l[i]) is not None:
            return [d [tar-l[i]],i]
        d[l[i]] = i
    print(d)


print(two_sum([2,7,11,15],9))
