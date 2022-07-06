def kth_sym(n):
    ret = ""
    if n==1:
        return "0"
    for a  in kth_sym(n-1):
        ret = ret +"01" if a=="0" else ret+"10"
    return ret

for a in range(10):
    print(kth_sym(a+1))
    print()



    