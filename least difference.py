def diff(arr1:list):
    arr = sorted(arr1)

    print(arr)
    diffe=arr[1]-arr[0]
    f =(arr[1],arr[0])
    for a in range(len(arr)-1):
        print(arr[a+1]-arr[a])
        if(diffe>(arr[a+1]-arr[a])):
            diffe= arr[a+1]-arr[a]
            f=(arr[a+1],arr[a])
    return (diffe,f)

print(diff([1,102,145,23,46,789,346,103]))

def rever(arr:list):
    b = len(arr)-1
    for a in range(0,int(len(arr)/2)):
        arr[a],arr[b-a]=arr[b-a],arr[a]
    return arr

print(rever([1,3,2,4,6,5]))