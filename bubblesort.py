def sorts(arr:list):
    step =0
    for b in range(len(arr)):
        for a in range(len(arr)-1):
            if(arr[a+1]<arr[a]):
                arr[a+1],arr[a]=arr[a],arr[a+1]
                print("step","\t",arr)


    return arr

print(sorts([7,5,1,2,7,0,9,6,7,0,9,0.78,-5]))
        
