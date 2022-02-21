

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.right = None
        self.left = None
    
    def insert(self, data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
            
    def get_root(self,data):
        if self.data:
            if self.left == data or self.right==data:
                return self.data
        
        
        
            
            
            
    def printtree(self):
        if self.left:
            self.left.printtree()
        print(self.data)
        if self.right:
            self.right.printtree()
            
        
    
        

if __name__ == "__main__":
    ab = Node(54)
    ab.insert(25)
    ab.insert(4)
    ab.insert(32)
    ab.insert(21)
    ab.insert(110)
    ab.insert(49)
    ab.printtree()
        
