

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
        self.previous = None
    
    def __str__(self) -> str:
        return str(self.data)

class LinkedList:
    def __init__(self,head=None) -> None:
        self.head = head
        
            
    def to_llist(self,l:list):
        llist = LinkedList()
        head_node = Node(l[0])
        llist.head = head_node
        llist.head.previous =None
        count=0
        temp_node = head_node
        while count!=len(l)-1:
            if count==0:
                llist.head.next=temp_node.next
                
            next_node = Node(l[count+1])
            temp_node.next=next_node
            next_node.previous=temp_node
            temp_node=temp_node.next
            count+=1
                
            
            
        return llist
               
    def reverse(self):
        
          
    
    def push(self,data):
        new_node = Node(data)
        new_node.previous = None
        self.head.previous=new_node
        new_node.next = self.head
        self.head = new_node
        
    def pop(self,index:int=None):
        
        if index is None:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            temp.next = None
            return        
        
        if index==0:
            if self.head:
                self.head = self.head.next
                self.head.previous = None
            else:raise IndexError
            return
        
        
        if index>0:
            count = 1
            temp = self.head
            tempp = None
            while count<=index:
                tempp=temp
                temp = temp.next
                count +=1

                
                if temp is None:raise IndexError("Sequence Index out of range")
                
            
            temp.next.previous = tempp
            tempp.next = temp.next
        

                
        
        
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
            
    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            new_node.previous=None
            self.head = new_node
            return
        temp = self.head
        tempp = self.head
        while temp:
            tempp = temp
            temp = temp.next
        new_node.previous = tempp
        tempp.next = new_node
        return
        
        
        
    def __str__(self) -> str:
        llist =""
        temp = self.head
        while temp:
            llist =llist+ f"({temp.previous},{temp.data},{temp.next})->"
            temp=temp.next
        return llist
            
def main():
    head = Node(1)
    second_data = Node(2)
    third_data = Node(3)
    head.next=second_data
    second_data.previous = head
    second_data.next = third_data
    third_data.previous=second_data
    linkedlist = LinkedList(head=head)
    linkedlist.push(5)
    linkedlist.push(6)
    linkedlist.append(4)
    linkedlist.append(5)
    linkedlist.push(33)
    linkedlist.pop(1)
    print(linkedlist)
    print(LinkedList().to_llist([0,1,2,3,4,5,6,7,8,9]))
    
main()
        
        