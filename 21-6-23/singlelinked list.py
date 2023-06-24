class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.last_Node = None
    def append(self,data):
        if self.last_Node is None:
            self.head = Node(data)
            self.last_Node = self.head
        else:
            self.head = Node(data)
            self.last_Node = self.last_Node.next
    def display(self):
        current = self.head
        while current is not None:
            print(current.data,end='')
            current = current.next
a_list = LinkedList()
n=int(input("enter the no.of elements:"))
for i in range(n):
    data = int(input("enter the elements:"))
    a_list.append(data)
    
print(" ",end='')
a_list.display()