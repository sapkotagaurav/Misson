'''d={}
nums=[1,1,2]
for a in nums:
    d[a]=d.get(a,0)+1
print(len(d.keys()),list(d.keys()))
    

a = {}
a.keys()

def revstring(string):
    toret = ""
    for a in range(len(string)):
        toret = toret + string[len(string)-1-a]
    return toret


def countKDifference( nums: list[int], k: int) -> int:
    dic = {}
    count = 0
    for num in nums:
        dic[num] = dic.get(num, 0)+1
        count += dic.get(num+k, 0)
        count += dic.get(num-k, 0)
    print(dic)
    return count

def lengthOfLastWord(self, s: str) -> int:
    s = s.strip()
    s_arr = s.split(" ")
    last_word=s_arr[len(s_arr)-1]
    return len(last_word)
print(countKDifference([1,2,3,4,5,0,3,7,8,9],2))

print([000,11,1,1].count(1))

def strStr( haystack: str, needle: str) -> int:
    needle_len=len(needle)
    if needle_len==0:return 0
    haystack_len=len(haystack)
    for a in range(haystack_len):
        print(haystack[a:a+needle_len])
        if haystack[a:needle_len-1]==needle:
            return a
    return -1


print(strStr("Nepal","ep"))



def merge_sorted(nums1:list,nums2:list):
    nums2.remove()

def checkifdouble(arr:list):
    for a in range(len(arr)-1):
        print(arr[a],arr.count(a))
        if arr.count(arr[a]*2):
            return True
    return False

print(checkifdouble([-2,0,10,-19,4,6,-8]))


def mountain_array(arr:list):
    print("max",max(arr))
    if len(arr)<3:return False
    i = 0
    if arr[i]>=arr[i+1]:return False
    while arr[i]<arr[i+1]:
        print(i,arr[i])
        i+=1
        if(i+1==len(arr)):return False
    for a in range(i,len(arr)-1):
        print(i,arr[i],arr[i+1])
        if arr[a]>arr[a+1]:
            
            continue
        return False
    return True

print(mountain_array([3,5,5]))

def calculate_cost():
    try:
        while True:
            x=int(input("Enter computer:"))
            y=int(input("Enter man:"))
            print(f"Cost={x*15+y*10}")
    except KeyboardInterrupt:
        print("Done")
        
calculate_cost()'''

def sortedSquares( nums: list[int]) -> list[int]:
    i =0
    j=0
    counter=0
    new_arr=[]
    for a in range(len(nums)-1):
        if nums[a]<0 and nums[a+1]>=0:
            i,j=a,a+1
            print(i>=0,j)
            break
    while i>=0 or j<len(nums): 
        if nums[i]**2 <nums[j]**2:
            new_arr.append(nums[i]**2)
            print(1,new_arr,i,j)
            i-=1
        else:
            new_arr.append(nums[j]**2)
            print(i,j,new_arr,2)
            j+=1
        if counter ==len(nums):break

        counter+=1
    return new_arr

#print(sortedSquares([-1,0,1]))
nums =[1,2,3,4,5,6,7]
k=3

nums=nums[len(nums)-k:len(nums)] +nums[0:len(nums)-k]
print(nums)


def isPower4(n:int)->bool:
    if n<=0:
        return False
    for a in range(0,n):
        if 4**a==n:
            return True
    return False
    