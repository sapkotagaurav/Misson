def norooms(arr:list):
    count =0
    for a in arr:
        if("+" in a):
            count +=1
    return count

print(norooms(["+1A","+2A","-3B"]))


'''
A program where time will be given in HH:MM format and we have to replace ? in order to find highest time
ex: ??:?? should return 23:59
?6:?7 should return 16:77

'''

def max_time(string):
    toreturn = ""
    if(string[0]=="?"):
        if(string[1]=="?"):
            toreturn+="2"
        elif(int(string[1])>=5):
            toreturn +="1"
        else:
            toreturn+="2"
    else:
        toreturn+=string[0]

    if(string[1]=="?"):
        if(int(toreturn[0])==2):
            toreturn+="3"
        else:
            toreturn+="9"
    else:
        toreturn += string[1]
    toreturn+=":"
    if(string[3]=="?"):
        toreturn+="5"
    else:
        toreturn+=string[3]
    if(string[4]=="?"):
        toreturn+="9"
    else:
        toreturn+=string[4]
    return toreturn

    

print(max_time(input("Enter time in(HH:MM format with ? sign somewhere:\n)")))