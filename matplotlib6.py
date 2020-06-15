import numpy as np
from matplotlib import pyplot as plt
x=np.arange(1,11)
y=2*x+5
plt.title("Using Matplotlib")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.plot(x,y)
plt.show()
