from array import *
arr=array('i',[10,20,30])
arr[1]=200
print(arr[1])

a=array('i',[5]*3)   #creating array of fixed size
print(a[2])

b=int(input("enter size of array"))
c=array('i',[0]*b)
print(c[2])
print("length of an array created ",len(c))