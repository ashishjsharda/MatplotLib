'''
Created on Jan 1, 2020

@author: ashish
'''

import matplotlib.pyplot as plt
google_stock=[1000,900,800,1200,1100]
year=[2012,2013,2014,2015,2016]
plt.plot(year,google_stock,'ok')
plt.xlabel("Year")
plt.ylabel("Price")
plt.title("Google Stock Price")
plt.show()
