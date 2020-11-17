'''This program is used to calculate the residue of given power'''


x = int(input("Enter the type of residue : "))
n = int(input("Enter the number to find the residue : "))
l = set({})
for i in range(1,n):
    if(i**x<n):
        print("{}**{} ≡ {}(mod {})".format(i,x,i**x,n))
        l.add(i**x)
    else:
        print("{}**{} ≡ {}=>{}(mod {})".format(i,x,i**x,(i**x)%n,n))
        l.add((i**x)%n)
print("Residue : ",l)
