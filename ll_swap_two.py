class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)
def printList(l):
    while l is not None:
        print(l.val, end="->")
        l=l.next
def swapTwo(a:ListNode):
    if a is None or a.next is None : return a
    a.val, a.next.val = a.next.val , a.val
    a.next.next = swapTwo(a.next.next)
    return a

def delete_at( prev_node):
    if prev_node is not None:
        prev_node.next = prev_node.next.next
        return
    else:
        raise IndexError

def pop(l):
    h = l
    while(h.next.next):
        h = h.next
    delete_at(h)

def reverseLL(l:ListNode):
    if l is None: return None
    temp = l
    if l.next:
        temp = reverseLL(l.next)
        l.next.next = l
    l.next = None
    return temp

def add_two(l1,l2):

    carry=0
    arr =[]
    l_ret = ListNode(5)
    if l1 and l2:
        if l1.val +l2.val + carry<10:
            l_ret = ListNode(val = l1.val+l2.val+carry)
            carry=0
        else:
            l_ret = ListNode(val =(l1.val+l2.val+carry)%10)
            carry = 1
        
        l_ret.next =add_two(l1.next,l2.next)
    else:l_ret.next = None
    return l_ret



def main():
    b = ListNode(val=4,next=None)
    m = ListNode(val =6,next =b)
    m1 = ListNode(val =5,next=m)
    m2 = ListNode(val =3,next=None)
    m3 = ListNode(val =4,next=m2)
    m4 = ListNode(val=2,next=m3)

    #printList(swapTwo(m4))
    print()
    print(type (add_two(m4,m1)))
    printList(add_two(m4,m1))

main()
