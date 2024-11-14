#two types direct ,indirect
#in direct func call itself only
# in case of indirect f1 call f2 

def factorial(x):
    if(x==0 or x==1):
        return 1
    else:
        return x*factorial(x-1)
    
print(factorial(3))