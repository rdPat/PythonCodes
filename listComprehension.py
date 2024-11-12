#concise way of writing list 

# i want list of squares from 1 to 10
from array import *
l=[x**2 for x in range(11)]
print(l)

#i want list of only even no
a=[x for x in range(11) if(x%2==0)]
print(a)