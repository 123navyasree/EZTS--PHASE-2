

#deletion of nodes
#first node deletion
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def delete(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def delete_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
    def delete_pos(self,posi):
        temp=self.head.next
        prev=self.head
        for i in range(1,posi-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
    def display(self):
        if self.head is None:
            print("List is Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" ")
                if temp.next!=None:
                    print('->',end="")
                temp=temp.next               
obj=SLL()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
obj.display()
print()
obj.delete()
obj.display()
print()
obj.delete_end()
obj.display()
print()
obj.delete_pos(2)
obj.display()
print()