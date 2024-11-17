import sys

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class link:
    def __init__(self):
        self.head=None
        
    def ins(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        tmp=self.head
        while tmp.next:
            tmp=tmp.next
        tmp.next=new_node

    def display(self):
        if self.head is None:
            print("ll is empty")
        tmp=self.head
        while tmp:
            print(tmp.data,"->",end=" ")
            tmp=tmp.next

    def findMax(self):
        if self.head is None:
            print("empty list")
            return
        tmp=self.head
        m=-sys.maxsize-1
        while tmp:
            if tmp.data>m:
                m=tmp.data
            tmp=tmp.next
        print("max value is",m)
    
    def findMiddle(self):
        sptr=self.head
        fptr=self.head

        while fptr and fptr.next:
            sptr=sptr.next
            fptr=fptr.next.next
        print("middle of ll is ",sptr.data)

    def identicalLL(self,otherll):
        a=self.head
        b=otherll.head
        while (a!=None) and (b!=None):
            if(a.data!=b.data):
                print("not identical")
                return
            a=a.next
            b=b.next
        print("identical",(a==None) and (b==None))

    def deleteNodeByVal(self,data):
        tmp=self.head
        if (self.head != None and self.head.data == data):
            self.head = self.head.next; 
            return
        
        #if tmp.data==data:
           # self.head=tmp.next
           # tmp.next=None
        prev=self.head
        while tmp:
            if(tmp.data==data):
                prev.next=tmp.next
                tmp.next=None
            tmp=tmp.next


l=link()
l.ins(100)
l.ins(200)
l.ins(300)
l.ins(400)
l.ins(500)
l.ins(600)
l.deleteNodeByVal(100)
l.display()

s=link()
s.ins(100)
s.ins(200)
s.ins(300)
s.ins(400)
s.ins(500)
s.ins(700)

#s.identicalLL(l)


#l.display()
#l.findMax()
#l.findMiddle()
