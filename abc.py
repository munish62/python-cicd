a=["abc","bcd","cde","def"]
b=[55,50,23,20]

family={}

for i in range(len(a)):
    print(i)
    family[a[i]] = b[i]
    
print(family)
