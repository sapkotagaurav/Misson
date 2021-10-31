class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
        

class LinkedList:
    def __init__(self) -> None:
         self.head = None
         
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def insertaf(self, prev_node:Node,new_data):
        if prev_node is None:
            raise IndexError
        
        newnode = Node(new_data)
        oldnode = prev_node.next
        prev_node.next = newnode
        newnode.next = oldnode
    
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
        self.head=self.head.next
        
    def delete(self,key):
        temp = self.head
        if(temp.data==key):
            self.head=temp.next
            return
        while(temp is not None):
            if(temp.data==key):
                break
            prev= temp
            temp = temp.next
            
        if temp == None:
            return
        prev.next = temp.next
        temp=None
    
    def delete_at(self,prev_node):
        if prev_node is not None:
            prev_node.next=prev_node.next.next
            return
        else:
            raise IndexError
        
    def pop(self):
        h = self.head
        while(h.next.next):
            h = h.next
        self.delete_at(h)
        
    def delete_pos(self,pos):
        count = 1
        temp = self.head
        if pos ==0:
            if self.head is not None:
                self.head = self.head.next
                
        else:
            while(count<=pos):
                if temp is None:
                    return
                else:
                    if count == pos:
                        temp.next = temp.next.next
                temp = temp.next
                count +=1
            
                    
            
        
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
        
         
if __name__ == "__main__":
    llist = LinkedList()
    firs = Node(1)
    llist.head = firs
  #  second = Node(2)
  # ''' third = Node(3)
  #  llist.head.next = second
   # second.next =third
   # third.next = Node(6) '''
   # llist.push(5)
    llist.insertaf(firs,8)
    llist.printlist()
    print("-------------")
    llist.append(54)
    llist.printlist()
    print("________________")
    llist.delete_first()
    llist.printlist()
    print("________________")
    llist.delete_at(llist.head)
    llist.append(54)
    llist.pop()
    llist.append(21)
    llist.push(1)
    llist.push(2)
    llist.push("hello")
    llist.push(3)
    llist.delete_pos(2)
    
    
    llist.printlist()