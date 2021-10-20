def num_ways(n):
    if n==1 or n==0:
        return 1

    result = num_ways(n-1) +num_ways(n-2)
    return result

print(num_ways(5))