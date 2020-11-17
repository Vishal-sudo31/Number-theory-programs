'''Using this program Euler Phi function of any number can be found'''
def GCD(x, y):
    while(y):
        x, y = y, x % y
    return x
def prime(a):
    for i in range(2,a//2):
        if(a%i==0):
            return False
    return True
n = int(input("Enter the number to find Euler Phi : "))
count = 0
if(prime(n)):
    print("\nEuler phi of {} = {}".format(n,n-1))
else:
    for i in range(1,n):
        if(GCD(i,n)==1):
            count+=1
    print("\nEuler phi of {} = {}".format(n,count))
