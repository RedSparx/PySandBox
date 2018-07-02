import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#region Define error surface within intervals for m and b.
N=50
m=np.linspace(-10,10,N)
b=np.linspace(-10,10,N)
mv,bv = np.meshgrid(m,b)
e2v=mv**2 + bv**2
#endregion

#region Create an arbitrary line with m and b defined within the intervals specified above.
m0=2
b0=-3
x0=np.linspace(-5,5,N)
y0=m0*x0+b
#endregion

#region Add an error to simulate data from a single experiment.
error=2.5*np.random.randn(N)
y1=y0+error
#endregion

#region Compute the error squared.
error2 = error**2
sum_error2=np.sum(error2)
#endregion

#region Produce plot of surface with the error on it.
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour(mv,bv,e2v,50)
#endregion

#region Produce plot of arbitrary line.
plt.figure()
plt.plot(x0,y0)
plt.plot(x0,y1,'r.')
plt.show()
#endregion
