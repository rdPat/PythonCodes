from array import *

arr=[[10,20],[30,40,50],[6,7,8],[9]]

#update 2 row in array
arr[1]=[2,2,2]

for a in arr:
    for b in a:
        print(b,end=" ")
    print(" ")

