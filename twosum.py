def twosum(array,target):
    for a in range(len(array)-1):
        for b in range(a+1,len(array)):
            if(array[a]+array[b]==target):
                return [a,b]
        
print(twosum([1,2,5,4,2,8,2,9,0],6))