import test
def reverse(string):
    s =""
    for a in range(len(string),0,-1):
        s= s +string[a-1]
    return s

def isPalindrome(string):
    if(string == reverse(string)):
        return True
    
    return False


def occourance(string,character):
    occ =0
    for a in string:
        if character ==a:
            occ+=1
    return occ

def matching_ele(arr):
    for a in range(0,len(arr)-1):
        for b in range(a+1,len(arr)):
            if(arr[a]==arr[b]):
                print(arr[a])
    
matching_ele([1,2,3,4,1,5,6,3])
#print(occourance("Pyaritika","i"))
#print(isPalindrome("racecar"))