def isvalid(string:str)->bool:
    stack=[]
    for a in string:
        if a in["{","[","("]:
            stack.append(a)
        else:
            if not stack:
                return False
            lastopened = stack.pop()
            if lastopened =="(":
                if a !=")":
                    return False
            if lastopened =="[":
                if a !="]":
                    return False
            if lastopened =="{":
                if a !="}":
                    return False
    if stack:
        return False
    return True

testcases =["[]({})[{}]","{{{}}}()","[({)}","()"]

for a in testcases:
    print(isvalid(a))
            