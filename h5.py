from cmath import nan
from math import fabs
from operator import index
from numpy import average
import pandas as pd
import matplotlib.pyplot as plt
def a(b):
    g=pd.DataFrame()
    while b=="yes":
        print("let's start")
        e=["ID.NO","NAME","SECTION","EG-MARKS","BEEE-MARKS","SM&DV-MARKS","NM-MARKS","TEC-MARKS","P&RV-MARKS"]
        d={i:[input(i+":")] for i in e}
        f=pd.DataFrame(d)
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
j=int(input("if you want to get only passed students data press-1 \n if you want to get only failed students data press-2"))
while j>0:    
    if j==1:
        k=k
        for x in k.index:
            l=["EG-MARKS","BEEE-MARKS","SM&DV-MARKS","NM-MARKS","TEC-MARKS","P&RV-MARKS"]
            for i in l:
                if k.loc[x,i]<18:
                    k.loc[x,i]=nan
        ps=k.dropna(inplace=False)
        print(ps)
        ps=ps.to_csv("ps.csv",index=False)
        #j=int(input("if you want to get only passed students data press-1 \n if you want to get only failed students data press-2"))
    elif j==2:
        k=k
        for x in k.index:
            l=["EG-MARKS","BEEE-MARKS","SM&DV-MARKS","NM-MARKS","TEC-MARKS","P&RV-MARKS"]
            if k.loc[x,l[0]]>17 and k.loc[x,l[1]]>17 and k.loc[x,l[2]]>17 and k.loc[x,l[3]]>17 and k.loc[x,l[4]]>17 and k.loc[x,l[5]]>17:
                k.loc[x,l[0]]=nan
        fs=k.dropna(inplace=False)
        print(fs)
        fs=fs.to_csv("fs.csv",index=False)
        #j=int(input("if you want to get only passed students data press-1 \n if you want to get only failed students data press-2"))
    else:
        n=int(input("if you want to get toatal marks of evrey student press-1\nif you want the grphical representation of the total marks of the student press-2\nif you want to campare the pass mean of the subjects press-3"))
        break
while n>0:
    k2=k[l].sum(axis=1)
    k["TOTAL"]=k2
    if n==1:
        print(k)
        n=int(input("if you want to get toatal marks of evrey student press-1\nif you want the grphical representation of the total marks of the student press-2\nif you want to campare the pass mean of the subjects press-3"))
    elif n==2:
        x=k["TOTAL"]
        y=k["ID.NO"]
        plt.plot(x,y,"*--r")
        plt.xlabel("TOTAL MARKS OF THE STUDENT")
        plt.ylabel("STUDENT ID")
        plt.title("GR OF TOTAL MARKS OF STUDENTS")
        plt.legend()
        plt.show()
        n=int(input("if you want to get toatal marks of evrey student press-1\nif you want the grphical representation of the total marks of the student press-2\nif you want to campare the pass mean of the subjects press-3"))
    elif n==3:
        x=["EG","BEEE","SM&DV","NM","TEC","P&RV"]
        l=["EG-MARKS","BEEE-MARKS","SM&DV-MARKS","NM-MARKS","TEC-MARKS","P&RV-MARKS"]
        p=[]
        for i in l:
            q=k[i].mean()
            p.append(q)
        plt.bar(x,p)
        plt.show()
        n=int(input("if you want to get toatal marks of evrey student press-1\nif you want the grphical representation of the total marks of the student press-2\nif you want to campare the pass mean of the subjects press-3"))

        