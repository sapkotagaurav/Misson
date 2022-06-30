def num_ways(n):
    phi=(1+5**0.5)/2
    phi_2=-1/phi
    ret = (phi**n -phi_2**n)/(5**0.5)
    return int(ret)
    

print(num_ways(3))