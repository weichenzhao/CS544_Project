import numpy as np
import matplotlib.pyplot as plt
#from matplotlib import mlab
import json

f = open('../cdf.txt', 'r')
cdf = []
for line in f:
    if line.split()[0] == "max":
        cdf.append(float(line.split()[5][:-1])) # percentage

num = len(cdf)
print num

x = np.array(range(num + 1)[1:])
y = np.array(cdf)

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.plot(x, y, '-', linewidth=1.5)
plt.grid(True)
plt.title('cumulative distribution for popular tags')


fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.plot(x, y, '-', linewidth=1.5)
plt.xscale('log')
plt.grid(True)
plt.ylim(0, 100)
plt.title('cumulative distribution for popular tags')

plt.show()
