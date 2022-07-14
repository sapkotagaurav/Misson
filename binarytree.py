

class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.right = None
        self.left = None
            
        
    
        

def levelorder(root):
    if root is None:
        return []
    if not root.left and not root. right:
        return root.val
    if root.left or root.right:
        a =[[root.val],[(levelorder(root.left)), levelorder(root.right)]]
        return a


if __name__ == "__main__":
    a=Node(5)
    a.left=b=Node(6)
    b.left = Node(4)
    a.right = Node(7)
    print(levelorder(a))
    

        
