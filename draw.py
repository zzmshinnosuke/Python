#coding=utf8
'''
Created on Apr 17, 2018

@author: zzm
'''
import Image
from matplotlib import pyplot as plt
from matplotlib.patches import Circle
img=Image.open('0.jpg')
img_gray=img.convert("L")
fig=plt.figure()

ax=fig.add_subplot(121) 
#第一个1代表一行，第二个2代表一列，第三个1代表，1行2列中的位置
'''
1 2
3 4
'''
ax.imshow(img)
ax.set_title("first")
#画线
pointx=[163,261,261,163,163]
pointy=[78,78,184,184,78]
ax.plot(pointx,pointy,'r')
#画点
ax.scatter(192,127)
ax.scatter(223,122)
#画圆
cir1=Circle(xy=(192,127),radius=20,alpha=0.1)
ax.add_patch(cir1)
plt.axis("off")

ax=fig.add_subplot(222)
ax.imshow(img_gray,cmap="gray")
ax.set_title("second")
plt.axis("off")


ax=fig.add_subplot(224)
ax.imshow(img_gray,cmap="gray") #以灰度图显示
ax.set_title("third")
plt.axis("off") #不显示刻度

plt.savefig("1.jpg") #如果放在plt.show()之后，会保存一张空图片
plt.show()
'''
或者先获取一下当前图片的‘句柄’
fig=plt.gcf()
plt.show()
fig.savefig('1.jpg',dpi=100)
'''


