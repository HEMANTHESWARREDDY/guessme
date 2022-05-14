def findWays(s,m):
    if (s == 0):
        return 1
    cnt = 0
    for i in range(1, m+1):
        while (s - i >= 0):
            cnt = cnt + findWays(s - i,m)
    return cnt
A=[]
for i in range(int(input())):
    s,m=int(input()),int(input())
    A.append([s,m])
for i in A:
    print(findWays(i[0],i[1]))
