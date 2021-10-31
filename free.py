def revstring(string):
    toret = ""
    for a in range(len(string)):
        toret = toret + string[len(string)-1-a]
    return toret

print(revstring("Gaurab"))
