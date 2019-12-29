'''
Created on Dec 29, 2019

@author: ashish
'''
from pylab import *
from numpy import *
x=linspace(-3, 3, 30)
y=x**2
xlabel("sin")
ylabel("cos")
title("Plots")
plot(x,sin(x))
plot(x,cos(x),'r-')
plot(x,-sin(x),'b-')
show()
