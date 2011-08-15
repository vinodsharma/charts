#!/usr/bin/env python
# a stacked bar plot with errorbars
import matplotlib
matplotlib.use('AGG') 
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(100, 50)) 

N = 5
latencies   = (20, 35, 30, 35, 27)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, latencies,   width, color='r')

plt.xlabel('number of workers')
plt.ylabel('latencies')
plt.title('latencies for http://www.google.com')
plt.xticks(ind+width/2., ('3','4','6','8','10'), horizontalalignment='center')
plt.yticks(np.arange(0,81,10))
fig.savefig('latency.png',dpi=10,transparent=False) 
#plt.show()


