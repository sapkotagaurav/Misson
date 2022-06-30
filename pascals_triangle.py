'''
                        1
                    1       1
                1       2       1
            1       3       3       1
        1       4       6       4       1
    1       5       10      10      5       1
1       6       15      20      15      6       1




'''
def getRow(self, rowIndex: int) -> list[int]:
    if rowIndex == 0: return [1]
    if rowIndex ==1 : return [1,1]
    l =[]
    t=self.getRow(rowIndex-1)
    for x in range(rowIndex-1):
       l.append(t[x]+t[x+1])
    return [1]+l+[1]
