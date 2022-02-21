'''A program to distribute candy to boys with array rating
each boy will get one more candy than the boy with less rating than him

example:[0,1,6] will return
1+2+3=6

[1,1,1,2,3,2+10]
=>1+1+1+2+2+3+4
'''





def distr(A:list):
    A= sorted(A)
    no_candy=1
    the_boy=0
    total_candy=0
    for boy in A:
        if the_boy == boy:
            total_candy = total_candy+ no_candy
            
        else:
            no_candy+=1
            total_candy+=no_candy
        the_boy = boy
    return total_candy


        
print(distr([3,5,2,7,9,2,2,0,3]))     
        