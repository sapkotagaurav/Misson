def sorts(arr:list):
    pivot = int(len(arr)/2)
    print(pivot)
    for a in range(pivot):
        if(arr[a]<arr[len(arr)-1-a]):
            arr[a],arr[len(arr)-1-a]=arr[len(arr)-a-1],arr[a]
    return arr

print(sorts([7,6,3,4,5]))