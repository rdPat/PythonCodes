#unordered mutable dont allow duplicates
course={"name":"java","version":"17"}
print(course)

#other way to create dictionary
a=dict([(1,1),(2,2),(3,11)])
print(a[1]) #a[key]
print(a.get(3))# to get data with key 3

#add new data into dictionary
a[4]="fourth"
print(a)
# update 
a[4]="fifth"
print(a)

#pop from dictionary
a.pop(4) #a.pop(key)
print(a)

#iterate
for k,v in a.items():
    print(k,v)
print("-----")
for k in a:
    print(k,a[k])

#get key only
for key in a.keys():
    print(key)

    print("-----")
#get value only sequentially
for v in a.values():
    print(v)

#length of dictionary
print("length",len(a))

#converting dict to string
print("dict->string",str(a))

#type of dict
print("type of dict",type(a))