#we can not add remove modify in tuple so better to first create list of it and perform action

t=(1,2,3,4,5,6)
l=list(t)
print("tuple-> list",l)
l.append(100)
l.sort(reverse=True)
print(l)
print("list->tuple",tuple(l))

#unpacking tuples
t1=(1,"name1","addr")
(id,name,add)=t1
print("id",id)
print("name",name)
print("addr",add)
