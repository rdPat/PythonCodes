a=[1,2,3,4,5]
b=[1,2,3,4,5]
c=a+b
print(c)

d=a*3
e=a[0:2]
print(e)
# function for list
arr=[1,2,3,4,4,4,4,4,5]
c=[100,200]
arr.append(10)

b=arr.copy()
print(id(arr))
print(id(b))

print("çount",arr.count(4))

arr.extend(c)
print(arr)

print("index of 100 :",arr.index(100))

arr.insert(1,555)
print(arr)

#pop return last element of list and delete it

arr.pop()
arr.pop()
arr.pop()
print(arr)


#remove function return very first occurence of element

e=[1,22,3,4,4,5]
e.remove(4)
print(e)

#reverse function

arr.reverse()
print("reversed",arr)
arr.reverse()
print("reversed",arr)
# partial reverse array while rotating array
# left rotate , right rotate by d steps 
#left rotation

k=int(input("enter k steps for left rotation :"))
s=[1,2,3,4,5]
n=len(s)
if k<n:
    s[0:k-1]=s[0:k-1][::-1]
    s[k:n]=s[k:n][::-1]
    s[0:n]=s[0:n][::-1]
print("left rotated ",s)


arr[1:3]=arr[1:3][::-1]
print(arr)

#sort
e=[25,3,2,-1,-1,22]
e.sort()
e.sort(reverse=True)  #for descending order
print(e)

#arr.clear()

