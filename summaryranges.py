def summary_ranges(nums):
    stk =[]
    stri=""
    start = False
    for a in range(len(nums)-1):
        
        if nums[a+1] -1 == nums[a] and not start:
            stri = str(nums[a]) + "=>" if not start else stri
            start = True
        else:
            if start:
                stri = stri + str(nums[a])
                start = False
        stk.append(stri)
    return stk


print(summary_ranges([1,2,3,4,6,8,9]))

            


