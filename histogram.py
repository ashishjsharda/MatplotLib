#Histogram
import numpy as np
from matplotlib import pyplot as plt
a=np.array([5,2,8,10,12,18,20,28])
plt.hist(a,bins=[0,5,10,15,20,25,30])
plt.title("Histogram")
plt.show()
