import sys
class Stack:
    def __init__(self,size):
        self.list=[None]*size
        self.capacity=size
        self.top=-1
    def push(self,data):
        #is full function
        if self.isFull():
            print("stack overflow")
        print("inserting into stack")
        self.top=self.top+1
        self.list[self.top]=data
 

    def pop(self):
        if self.isEmpty():
            print("underflow")
        print("deleting element",self.peek())
        self.top=self.top-1

    def peek(self):
        if self.isEmpty():
            exit(-1)
        return self.list[self.top]
    
    def size(self):
        return self.top+1
    def isEmpty(self):
        return self.size()==0
    def isFull(self):
        return self.capacity==self.size()
    def display(self):
        i=self.size()
        j=0
        while j<i:
            print(self.list[j])
            j=j+1
    def findMax(self):
        m=-sys.maxsize-1
        tmp=self.top
        i=self.size()-1
        while i>0:
            if m<self.list[i]:
                m=self.list[i]
            i=i-1
        print("maximum",m)

    
s=Stack(3)
s.push(10)
s.push(20)
s.push(300)
s.findMax()
#s.pop()
s.display()
        



    
    

    