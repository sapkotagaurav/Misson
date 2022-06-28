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

def reverseLL(l:ListNode):
    if l is None or l.next is None : return l
    last= l
    oneless = ListNode(l.val)
    temp =l
    while last.next is not None:
        last = last.next
    while temp.next != last:
        oneless.val=temp
        temp = temp.next
    last.next = reverseLL(oneless)
    return last
    



def main():
    b = ListNode(val=5)
    m = ListNode(val =4,next =b)
    m1 = ListNode(val =3,next=m)
    m2 = ListNode(val =2,next=m1)
    m3 = ListNode(val =1,next=m2)
    m4 = ListNode(val=0,next=m3)

    printList(swapTwo(m4))
    print()
    printList(reverseLL(m4))

main()
