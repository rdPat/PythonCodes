a=[1,2,2,3,4,-1,-11]
print(max(a))
print(min(a))

lmax=lmin=a[0]
for x in a:
    if x>lmax:
        lmax=x
    if x<lmin:
        lmin=x
print(lmax,lmin)