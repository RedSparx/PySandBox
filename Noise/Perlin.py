from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from noise import pnoise2, snoise2
from PIL import Image
import pylab
import sys
import csv

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

#region Define Perlin noise parameters and generate a random surface.
Octaves=40
Frequency=8*Octaves
Persistance=0.2
Lacunarity=5.1
Array_Size=600

PNoise = np.empty((Array_Size,Array_Size))
for i in range(0,PNoise.shape[0]):
    for j in range(0,PNoise.shape[1]):
        PNoise[i,j]=pnoise2(i/Frequency,j/Frequency,Octaves,Persistance,Lacunarity)
xx, yy = np.mgrid[0:PNoise.shape[0], 0:PNoise.shape[1]]
#endregion

#region Plot the Perlin noise as a surface so that the "terrain" can be visualized.
fig = plt.figure()
ax = fig.gca(projection='3d')
# PNoise[PNoise<=0]=np.nan
surf = ax.plot_surface(xx, yy, PNoise, cmap=cm.jet,\
                       linewidth=2, antialiased=False,\
                       rcount=100,ccount=100)
                        #,vmin=-1.0,vmax=+1.0)
ax.set_axis_off()
plt.show()
#endregion

#region Write the data to CSV.
#np.savetxt("Perlin_Terrain.csv", PNoise, delimiter=',')
f=open('Perlin_Terrain.csv','wt')
f.write('X,Y,Z\n')
for i in range(0,PNoise.shape[0]):
    for j in range(0,PNoise.shape[1]):
        f.write('%d,%d,%f\n'%(i,j,PNoise[i,j]))
f.close()
#endregion

