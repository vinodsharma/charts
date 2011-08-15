import numpy as np
import matplotlib.pyplot as plt

fig1 =plt.figure(figsize=(10,5))


conf1_latencies = [10,15,12,13,11,17,15]
conf2_latencies = [8,10,6,8,10,14,17]
conf3_latencies = [9,11,10,12,11,13,9]
num_workers = [3,6,9,12,15,18,21]
plt.xlabel('number of workers')
plt.ylabel('latency(ms)')
plt.title('latencies for http://www.google.com')
line1, = plt.plot(num_workers,conf1_latencies, 'r-o')
line2, = plt.plot(num_workers,conf2_latencies, 'g-o')
line3, = plt.plot(num_workers,conf3_latencies, 'b-o')
plt.legend( (line1, line2, line3),('conf1', 'conf2', 'conf3'), loc='best')
plt.xticks((np.arange(0,30)))
plt.yticks(np.arange(0,20))
plt.savefig("test.png", format='png') # note the format='pdf' argument!
plt.close()


