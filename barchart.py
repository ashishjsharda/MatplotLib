import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
langs=["C","C++","Java","Python","PHP"]
students=[29,39,19,42,59]
ax.bar(langs,students)
plt.show()
