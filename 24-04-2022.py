from ast import While
from cmath import nan
from operator import index
from re import M
from numpy import False_
import pandas as pd
def a(b):
    m=[]
    g=pd.DataFrame()
    while b=="yes":
        print("let's start")
        c=int(input("GIVE YOU RG.NO"))
        c="211FA1"+str(c)
        m.append(c)
        e=["NAME","SECTION","EG-MARKS","BEEE-MARKS","SM&DV-MARKS","NM-MARKS","TEC-MARKS","P&RV-MARKS"]
        d={i:[input(i+":")] for i in e}
        f=pd.DataFrame(d,index=[c])
        h=[g,f]
        i=pd.concat(h)
        #print(i)
        g=i
        b=input("enter again\n YES/NO")
        if b=="no":
            break
    else:
        "po ra pooka"
    # print(g)
    k=g.to_csv("a.csv",index=False)
    k=pd.read_csv("a.csv")
    return k
k=a(input("would you like to share your data:\n YES/NO"))
print(k)
j=int(input("if you want to get only passed students data press 1 \n if you want to get only failed students data press 2 "))
if j==1:
    for x in k.index:
        l=["EG-MARKS","BEEE-MARKS","SM&DV-MARKS","NM-MARKS","TEC-MARKS","P&RV-MARKS"]
        for i in l:
            if k.loc[x,i]<18:
                k.loc[x,i]=nan
    k.dropna(inplace=True)
    print(k)
elif j==2:
    for x in k.index:
        l=["EG-MARKS","BEEE-MARKS","SM&DV-MARKS","NM-MARKS","TEC-MARKS","P&RV-MARKS"]
        for i in l:
            if k.loc[x,i]>17:
                k.loc[x,i]=nan
    k.dropna(inplace=True)
    print(k)