def take_input():
    lista =[]
    while True:
        try:
            x = int(input("Enter a integer:\t"))
            lista.append(x)
        except ValueError:
            break
    return lista


def sortem(lista):
    for a in range(0, len(lista)-1):
        minimum =a
        for b in range(a+1,len(lista)):
            if(lista[b]<lista[minimum]):
                minimum = b
        if(a!=minimum):
            lista[a],lista[minimum]=lista[minimum],lista[a]
    
    return lista


print(sortem(take_input()))