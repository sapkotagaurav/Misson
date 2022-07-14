def product_except_self(nums):
    mul =1
    ret =[]
    for a in nums:
        mul *=a
    for x in nums:
        if x==0:
            ret.append(int(mul*1**(-1)))
        else:
            ret.append(int(mul*x**(-1)))

    return ret
    


print(product_except_self([-1,1,0,-3,3]))