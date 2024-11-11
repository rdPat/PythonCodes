# how to create 2d array
from array import *
arr=[[10,20],[30,40,50],[6,7,8],[9]]
print(len(arr))
#for i in range(len(arr)):
#    print(arr[i])
for a in arr:
    for b in a:
        print(b,end=" ")
    print(" ")

#insert in 2d array

arr.insert(0,[10,20,30])
arr[1][1]=40
#delete from 2d array

del(arr[0])  
print("-------")
for c in arr:
    for d in c:
        print(d,end=" ")
    print(" ")





