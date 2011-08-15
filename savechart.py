import matplotlib 
matplotlib.use('Agg') 
from matplotlib import pyplot as plt 

fig = plt.figure(figsize=(23.5, 13.0)) 
ax = plt.axes([0.0, 0.0, 1.0, 1.0]) 
ax.plot([1, 2, 4], lw=5) 
ax.set_xticks([]) 
ax.set_yticks([]) 

fig.savefig('test.jpg', dpi=10) 

