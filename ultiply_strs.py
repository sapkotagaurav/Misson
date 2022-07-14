def multiply(s1,s2):
        num_1=0
        num_2=0
        d = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,}
        for a in s1:
            num_1 = num_1*10+d.get(a)
            print(num_1,a,d.get(a))
        for a in s2:
            num_2 = num_2*10+d.get(a)
        print(num_1,num_2)
        return str(num_1*num_2)


print(multiply("123","456"))