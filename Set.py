#separated by comma, no duplicate , immutable
a={1,2,3,2}
print(a)
b=[1,22,21,1]
c=set(b)
print("list->set",c)
# create empty set
e=set()
print(e)

#checking particular element present in set or not
y={100,20,300,400}
x=int(input("enter no:"))
flag=x in y
print(flag)