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
    sum = ListNode(0)
    cur = sum

    carry=0
    while l1 or l2 or carry:
        tot= carry
        if l1:
            tot += l1.val
            l1=l1.next
        if l2:
            tot+=l2.val
            l2 =l2.next
        carry = tot//10
        res =  tot%10
        cur.next = ListNode(res)
        cur = cur.next
    return sum.next


def toLL(l):
    if not l:
        return None
    ret = ListNode(l[0])
    ret.next = toLL(l[1:])
    return ret


def merge_two_sorted(l1,l2):
    ret = None
    if not l1:
        return l2
    
    if not l2:
        return l1
    
    ret = l1 if l1.val< l2.val else l2
    if l1.val < l2.val:
        ret.next = merge_two_sorted(l1.next,l2)
    else:
        ret.next = merge_two_sorted(l1,l2.next)
    return ret



def main():
    b = ListNode(val=4,next=None)
    m = ListNode(val =6,next =b)
    m1 = ListNode(val =5,next=m)
    m2 = ListNode(val =3,next=None)
    m3 = ListNode(val =4,next=m2)
    m4 = ListNode(val=2,next=m3)

    #printList(swapTwo(m4))
    print()
    #print(type (add_two(m4,m1)))
    #printList(add_two(m4,m1))

    a = toLL([9,9,9,9])
    b = toLL([9,9])
    printList(add_two(a,b))

main()
