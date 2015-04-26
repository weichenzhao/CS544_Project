import numpy as np
import matplotlib.pyplot as plt
#from matplotlib import mlab
import json

def read_data(name):
    f = open(name, 'r')
    ret = []
    for line in f:
        ret.append(float(line))
    return ret


train = read_data('train_dist.txt')
test = read_data('test_dist.txt')
orig = read_data('original_dist.txt')

num = len(train)

x = np.array(range(num + 1)[1:])
y1 = np.array(train)
y2 = np.array(test)
y3 = np.array(orig)

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
plot1 = ax1.plot(x, y1, linewidth=1.5, color='r')
plot2 = ax1.plot(x, y2, linewidth=1.5)
plot3 = ax1.plot(x, y3, linewidth=1.5)
#plt.yscale('log')
plt.grid(True)
plt.legend(['training data', 'test data','original data'], loc=0, prop={'size':9})
plt.ylabel('Percentage')
plt.xlabel('Index of popular tags')

"""
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
plot1 = ax2.plot(x1, y1, '-', linewidth=1.5)
plot2 = ax2.plot(x2, y2, '--', linewidth=1.5)
plt.xscale('log')
plt.grid(True)
plt.ylim(0, 100)
"""
#plt.title('')
#plt.legend((plot1, plot2), ('label1, label2'), 'best', numpoints=1)
#plt.legend(['best possible f1 score\n(tag CDF)', 'question coverage'], loc=0, prop={'size':9})
#plt.ylabel('Percentage')
#plt.xlabel('Number of popular tags')

plt.show()
