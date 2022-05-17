
def findWays(s,m):
    if (s == 0):
        print(1)
    cnt = 0
    for i in range(1, m+1):
        if (s - i >= 0):
            cnt = cnt + findWays(s - i,m)
    print(cnt)
A=[]
for i in range(int(input())):
    s,m=(int(i) for i in input().split())
    A.append([s,m])
for i in A:
    s,m=i[0],i[1]
    if (s == 0):
        print(1)
    cnt = 0
    for i in range(1, m+1):
        if (s - i >= 0):
            cnt = cnt + findWays(s - i,m)
    print(cnt)

