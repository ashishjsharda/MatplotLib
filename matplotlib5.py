'''
Created on Jan 11, 2020
Using Matplotlib
@author: ashish
'''
from matplotlib import pyplot as plt
x=[2,4,6]
y=[1,4,7]
x2=[8,10,12]
y2=[3,5,9]
plt.bar(x,y,align="center")
plt.bar(x2,y2,align="center")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Bar Chart")
plt.show()
