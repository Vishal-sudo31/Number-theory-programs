def modInverse(a, m): 
    a = a % m 
    for x in range(1, m): 
        if ((a * x) % m == 1): 
            return x 
    return 1
for i in range(1,26):
    print(i,'-', modInverse(i, 26))
#print(modInverse(a, m))
