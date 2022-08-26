def product_except_self(nums):
        n=len(nums)
        left=[]
        right=[]
        output=[]
        for a in range(n):
            print(n-a)
            right.insert(0,nums[n-1] if a==0 else right[0]*nums[n-a-1])
            if a==0:
                left.append(nums[a])

            else:
                left.append(left[a-1]*nums[a])

        for a in range(n):
            if(a==0):
                output.append(right[a+1])
            elif(a==n-1):
                output.append(left[a-1])
            else:
                output.append(right[a+1]*left[a-1])

        return output

print(product_except_self([1,3,0,5,4]))


