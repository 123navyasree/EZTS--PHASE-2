#search the node in list
'''class Node:
    def _init_(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def _init_(self):
        self.head=None
    def search(self,num):
        temp=self.head
        while temp:
            temp.data=num
            print("yes")
            break
        temp=temp.next
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
obj.head.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
obj.display()
print("")
obj.search(20)
print("")'''