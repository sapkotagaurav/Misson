import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    if root is None : return 0
    else:
        ldepth = maxDepth(root.left)
        rdepth = maxDepth(root.right)

        if (ldepth > rdepth):
            return ldepth +1
        else:
            return rdepth +1

    
def main():
    ae = TreeNode(9)
    ae1 = TreeNode(15)
    ae2 = TreeNode(7)
    ae3 = TreeNode(20,left=ae2,right=ae1)
    ae4 = TreeNode(3, left=ae3,right=ae1)
    print(maxDepth(ae4))

main()

math.e