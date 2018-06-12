import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.colors as colors
n=10
m=20
#x=np.arange(0,n,0.5)
#y=np.arange(0,n,math.sqrt(3)/2)
x_list=[]
y_list=[]
t_list=[]

for i in range(0,n+1):
    x_list.append(i)
    y_list.append(i)

p_map = np.zeros([n+1,n+1])
next_p_map=np.zeros([n+1,n+1])
p_map[0,0]=1
next_p_map[0,0]=1
for t in range(0,m):
    t_list.append(t)
    if t ==0:
        p_map
    else:
        next_p_map
        for x in range(0,n+1):
            if x ==0:
                for y in range(0,n+1):
                    if y ==0:
                        next_p_map[x,y]=(p_map[x,y+1])*(1/2)+(p_map[x+1,y])*(1/2)
                    elif y==n:
                        next_p_map[x,y]=(p_map[x,y-1])*(1/2)+(p_map[x+1,y])*(1/2)
                    else:
                        next_p_map[x,y]=(p_map[x,y+1])*(1/3)+(p_map[x+1,y])*(1/3)+(p_map[x,y-1])*(1/3)
            elif x ==n:
                for y in range(0,n+1):
                    if y ==0:
                        next_p_map[x,y]=(p_map[x-1,y])*(1/2)+(p_map[x,y+1])*(1/2)
                    elif y==n:
                        next_p_map[x,y]=(p_map[x-1,y])*(1/2)+(p_map[x,y-1])*(1/2)
                    else:
                        next_p_map[x,y]=(p_map[x,y+1])*(1/3)+(p_map[x-1,y])*(1/3)+(p_map[x,y-1])*(1/3)
            else:
                for y in range(0,n+1):
                    if y ==0:
                        next_p_map[x,y]=(p_map[x-1,y])*(1/3)+(p_map[x+1,y])*(1/3)+(p_map[x,y+1])*(1/3)
                    elif y==n:
                        next_p_map[x,y]=(p_map[x-1,y])*(1/3)+(p_map[x+1,y])*(1/3)+(p_map[x,y-1])*(1/3)
                    else:
                        next_p_map[x,y]=(p_map[x,y+1])*(1/4)+(p_map[x-1,y])*(1/4)+(p_map[x,y-1])*(1/4)+(p_map[x+1,y])*(1/4)
        p_map = next_p_map
    print(t,p_map)




#plot
fig=plt.figure()
ax = Axes3D(fig)
X,Y = np.meshgrid(x_list,y_list)
ax.set_xlim(n,0)
ax.set_ylim(0,n)
ax.set_zlim(-0.02,0.03)

#Z軸の色を設定
#offset = p_map.ravel() + np.abs(p_map.min())
#fracs = offset.astype(float)/offset.max()
#norm = colors.Normalize(fracs.min(), fracs.max())
#clrs = cm.cool(norm(fracs))
#ax.bar3d(X.ravel(), Y.ravel(), p_map.ravel() ,0.1, 0.1, -p_map.ravel(),color =clrs)#,cmap=cm.hot)
ax.w_xaxis.set_pane_color((0, 0, 0, 0))
ax.w_yaxis.set_pane_color((0, 0, 0, 0))
ax.w_zaxis.set_pane_color((0, 0, 0, 0))
#plt.show()

#surface
surf = ax.plot_surface(X, Y, p_map, cmap =cm.coolwarm , linewidth=0)
fig.colorbar(surf)
plt.show()
