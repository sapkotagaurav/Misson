def maxArea(height):
    a =[]
    for x in range(len(height)):
        for y in range(x+1,len(height)):
            a.append(min(height[x],height[y])*(y-x))
    return max(a)


#Leetcode https://leetcode.com/problems/container-with-most-water/

def maxArea2(h:list):
    #two pointer approach

    ret ,i ,j = 0,0,len(h)-1

    while i<j:
        ans = max(ans,min(h[i],h[j])*(j-i))
        if h[i]<h[j]:
            i+=1
        else:
            j-=1
    return ans






