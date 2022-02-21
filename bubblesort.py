def sorts(arr:list):
    step =0
    for b in range(len(arr)):
        for a in range(len(arr)-1):
            if(arr[a+1]<arr[a]):
                arr[a+1],arr[a]=arr[a],arr[a+1]
                print("step","\t",arr)


    return arr


'''Insertion sort'''
def insertion_sort(arr:list):
    for a in range(len(arr)):
        x = arr[a]
        j = a -1
        while j>=0 and arr[j]> x:
            arr[j+1]= arr[j]
            j-=1
        arr[j+1]=x
    
        
