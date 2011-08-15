import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# Make an example plot with two subplots...
fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax1.plot(range(10), 'b-')

# Save the full figure...
fig.savefig('full_figure.png')

