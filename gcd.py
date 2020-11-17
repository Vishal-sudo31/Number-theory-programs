'''This program is for calulating gcd with visible steps..'''

m,n = map(int,input("Enter the numbers : ").split())
y = 1
while(y!=0):
    x,y = m//n,m%n
    print("{}={}.{}+{}".format(m,x,n,y),end="\n")
    m,n = n,y


