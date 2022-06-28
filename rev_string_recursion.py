from re import S


def revString(s:list):
    stack =[]
    i=0
    for c in s:
        stack.append(c)

    while stack:
        s[i] = stack.pop()
        i+=1

    return s

print(revString(["H","E","L","L","O"]))

