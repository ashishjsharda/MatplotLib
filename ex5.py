'''
Created on Dec 30, 2019

@author: ashish
'''
import matplotlib.pyplot as plt
appl=[90,70,110,120]
years=[2016,2017,2018,2019]
msft=[50,40,70,80]
plt.xlabel("Years")
plt.ylabel("Price")
plt.title("Stock Prices Over Years")
plt.plot(years,appl,'k',years,msft,'g')
plt.show()
