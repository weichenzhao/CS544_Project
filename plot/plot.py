import numpy as np
import matplotlib.pyplot as plt
#from matplotlib import mlab
import json

f = open('../cdf.txt', 'r')
cdf = []
for line in f:
    if line.split()[0] == "max":
        cdf.append(float(line.split()[5][:-1])) # percentage

f2 = open('file_cov.txt', 'r')
cov = []
for line in f2:
    cov.append(float(line)) # percentage

num1 = len(cdf)
num2 = len(cov)

x1 = np.array(range(num1 + 1)[1:])
x2 = np.array(range(num2 + 1)[1:])
y1 = np.array(cdf)
y2 = np.array(cov)

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
plot1 = ax1.plot(x1, y1, '-', linewidth=1.5)
plot2 = ax1.plot(x2, y2, '--', linewidth=1.5)
plt.grid(True)
#plt.title('')
plt.legend(['best possible f1 score\n(tag CDF)', 'question coverage'], loc=4, prop={'size':9})
plt.ylabel('Percentage')
plt.xlabel('Number of popular tags')


fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
plot1 = ax2.plot(x1, y1, '-', linewidth=1.5)
plot2 = ax2.plot(x2, y2, '--', linewidth=1.5)
plt.xscale('log')
plt.grid(True)
plt.ylim(0, 100)
#plt.title('')
#plt.legend((plot1, plot2), ('label1, label2'), 'best', numpoints=1)
plt.legend(['best possible f1 score\n(tag CDF)', 'question coverage'], loc=0, prop={'size':9})
plt.ylabel('Percentage')
plt.xlabel('Number of popular tags')

plt.show()
