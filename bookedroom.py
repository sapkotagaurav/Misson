def norooms(arr:list):
    count =0
    for a in arr:
        if("+" in a):
            count +=1
    return count

print(norooms(["+1A","+2A","-3B"]))

def max_time(string):
    string[4] = "9" if string[4]=="?" else string[4] 
    return string

print(max_time(list("23:5?")))