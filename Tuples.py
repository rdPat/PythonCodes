#ordered list
t1=(1,2,2,3)
print(t1)
t2=(2,2,2,1)
print(t1+t2)

a=[1,"r"]
print(a)

t=(2,"p")
print(t)

#check for item present in it
t=("ab","b",100,1.1)
if "a" in t:
    print("a found at",t.index("a"))
else:
    print("a not found")

#get particular range of tuple 
t2=(1,2,3,4.5)
print(t2[0:2:2])   # [start:end:jump]

print(t2[2:])


