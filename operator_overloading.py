class Animals:
    def __init__(self,group,name) -> None:
        self.group = group
        self.name = name
    
    def __str__(self) -> str:
        return f"{self.name} : {self.group}"
    
    def __add__(self,other):
        new_group = self.group.copy()
        new_group.append(other)
        return Animals(new_group,self.name)
    
a = Animals(["Dog","Cat"],"Mammals")
b = a + "bat"
print(b)

