# how to create sll

# create a node
class Node:
    def __init__(self,data):
      self.data=data
      self.next=None

class ll:
   def __init__(self):
      self.head=None

   def insert_at_end(self,data):
      new_node=Node(data)
      if self.head is None:
         self.head=new_node
         return
      current=self.head
      while current.next:
         current=current.next
      current.next=new_node

   def insert_at_begining(self,data):
      new_node=Node(data)
      new_node.next=self.head
      self.head=new_node
   def display(self):
      current=self.head
      while current:
         print(current.data,"->",end=" ")
         current=current.next
   def length(self):
      current=self.head
      le=0
      while current:
         le=le+1
         current=current.next
      return le
   def deleteNode(self,value):
      if self.head is None:
         print("list is empty")
      if self.head.data==value:
         self.head=self.head.next
         return
      new_node=self.head
      for i in range(3):
         while new_node:
            if new_node.data!=value:
               new_node=new_node.next

         if new_node.next is None:
            print("no data found")
         else:
            new_node.next=new_node.next.next
      
   def RemoveElement(self,value):
      dumbhead=Node(None)
      dumbhead.next=self.head

      tmp=dumbhead
      while tmp.next:
         if tmp.next.data==value:
            tmp.next=tmp.next.next
         else:
            tmp=tmp.next
      return dumbhead.next







l=ll()
#l.insert_at_begining(30) 
l.insert_at_end(20)
l.insert_at_end(20)
l.display()
print(l.length())
#l.deleteNode(20)
l.RemoveElement(20)
l.display()
print(l.length())
      

      

 