from cProfile import label
from matplotlib import projections
import matplotlib.pylab as plt
from matplotlib.pyplot import xlabel
x=[3,4,5,6,7,8,9,10]
y=[1,2,3,4,5,6,7,8]
z=[0,1,2,3,4,5,6,7]
plt.figure(figsize=(10,8))
ax=plt.axes(projection="3d")
fg=ax.scatter3D(x,y,z,c=y,label="bobby,hemanth,eswar")
a={"family":"serif","color":"blue","size":20}
font1 = {'family':'serif','color':'blue','size':20}
plt.title("bobby",fontdict=a)
plt.xlabel("hemanth",fontdict=a)
plt.ylabel("eswar",fontdict=a)
plt.legend()
plt.show()