from math import gcd
def gcd(a,b):
    if (b==0):
        return a
    return gcd (b, a%b)
n=int(input())
a=[int(i) for i in input().split()]
m=int(input())
q=[int(i) for i in input().split()]
for i in range(len(a)):
    print(gcd(a[i],q[i]-a[i]))

