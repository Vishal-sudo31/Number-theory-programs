a=[]
m=[]
def chinese(n):
    b1=[]
    b2=[]
    M=1
    y=0
    for i in range(n):
       M = M * m[i]
    for i in range(n):
        b1.append(M / m[i])
        b2.append(modInverse(b1[i],m[i]))
    print(b2)
    for i in range(n):
        x =int( a[i] * b1[i] * b2[i])
        y = y + x
    print("X = ",y)
    y = y % M
    print(y ," mod ", M)
def modInverse(a, m): 
    a = a % m; 
    for x in range(1, m):
        if ((a * x) % m == 1):
            return x 
    return 1
        
if __name__ == "__main__":
    n=int((input("How many equations you want:")))
    for i in range(n):
        print("Enter",i+1,"Equation values:")
        v = int(input("a:"))
        a.append(v)
        w=int(input("m:"))
        m.append(w)
    chinese(n)
