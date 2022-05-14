import random
k=int(input())
l=int(input())
d=[]
for i in range(k,l):
    d.append(i)
print(d)
e=[]
while 1>0:
    if len(e)==len(d):
        print(e)
        break
    else:
        f=random.randint(k,l)
        if f in d:
            continue
        else:
            e.append(f)
else:
    print("sorry")