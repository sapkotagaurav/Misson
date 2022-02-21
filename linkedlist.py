

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return str(self.data)


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def __str__(self) -> str:
        x = self.head
        ret = ""
        while x:
            ret += str(x.data) + "->"
            x = x.next
        return ret

    def swap(self, posX, posY):
        nX = self.get(posX)
        nY = self.get(posY)
        if nX.next and nY.next:
            temp = nX
            nX.next = nY.next
            nY.next = temp.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertaf(self, prev_node: Node, new_data):
        if prev_node is None:
            raise IndexError

        newnode = Node(new_data)
        oldnode = prev_node.next
        prev_node.next = newnode
        newnode.next = oldnode

    def get(self, pos: int):
        temp = self.head
        a = 0
        while a < pos:
            try:
                temp = temp.next
                a += 1
            except ValueError:
                raise IndexError()
        return temp

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        lastnode = self.head
        while(lastnode.next):
            lastnode = lastnode.next
        lastnode.next = new_node

    def delete_first(self):
        self.head = self.head.next

    def delete(self, key):
        temp = self.head
        if(temp.data == key):
            self.head = temp.next
            return
        while(temp is not None):
            if(temp.data == key):
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return
        prev.next = temp.next
        temp = None

    def delete_at(self, prev_node):
        if prev_node is not None:
            prev_node.next = prev_node.next.next
            return
        else:
            raise IndexError

    def pop(self):
        h = self.head
        while(h.next.next):
            h = h.next
        self.delete_at(h)

    def delete_pos(self, pos):
        count = 1
        temp = self.head
        if pos == 0:
            if self.head is not None:
                self.head = self.head.next

        else:
            while(count <= pos):
                if temp is None:
                    return
                else:
                    if count == pos:
                        temp.next = temp.next.next
                temp = temp.next
                count += 1

    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


def delete_dups(llist: LinkedList):
    d = {}
    temp = llist.head
    while temp:
        s = d.get(temp.data, 0)
        if s:
            if temp.next:
                temp.next = temp.next.next
            else:
                temp.next = None
                return
        else:
            d[temp.data] = d.get(temp.data, 0) + 1
        temp = temp.next


if __name__ == "__main__":
    llist = LinkedList()
    firs = Node(1)
    llist.head = firs

    sec = Node(2)
    firs.next = sec
    thir = Node(6)
    sec.next = thir
    fot = Node(4)
    thir.next = fot
    llist.append(1)
    llist.append(5)
    llist.append(6)
    llist.delete_pos(2)
    print(llist.get(0))

    print(llist)

    def sum_of_two(l1: Node, l2: Node) -> Node:
        n1 = 0
        n2=0
        temp = l1
        p = 0
        while temp is not None:
            n1 += temp.data *10**p
            p+=1
            temp = temp.next
        p = 0
        temp = l2
        while temp is not None:
            n2 += temp.data *10**p
            p+=1
            temp = temp.next
        s = n1+n2
        a=10
        k = None
        while s>0:
            
            f=s%a
            s=s//a
            k= Node(f)
            k=temp
            k = temp.next
            
            
            print(f)
            
            
        return [k,k.next,k.next.next]
    
        
l1=Node(2)
la=Node(4)
lb=Node(3)
la.next=lb
l1.next=la
l2=Node(5)
l2a=Node(6)
l2b=Node(4)
l2a.next=l2b
l2.next=l2a    
print(sum_of_two(l1,l2))                
            
        
        
                
            
            
    
    