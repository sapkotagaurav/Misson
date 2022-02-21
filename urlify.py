def f(s:str):
    s =s.strip()
    a = s.count(" ")
    print(a)
    for m in range(a):
        s =s.replace(" ","%20")
    return s

print(f("My name is gaurab sapkota and i suck"))