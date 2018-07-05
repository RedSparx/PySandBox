import numpy as np
import matplotlib.pyplot as plt

#region Create N random vectors of dimension D and compute the corelation matrix S.
N1=200 # Number of Gaussian points.
N2=200 # Number of Gaussian points.
N3=200  # Number of Gaussian points.
N4=0  # Number of uniform points.
N=N1+N2+N3+N4 # Total number of points.
D=2 # Dimension.
# Generate vectors separately then append them.
V1 = [0.05, 0.05] * np.random.randn(N1,D) + [[np.random.randn(),np.random.randn()]] * N1
V2 = [0.04, 0.04] * np.random.randn(N2,D) + [[np.random.randn(),np.random.randn()]] * N2
V3 = [0.06, 0.03] * np.random.randn(N3,D) + [[np.random.randn(),np.random.randn()]] * N3
V4 = np.random.randn(N4,D) - 0.5
V = np.append(V1,V2,axis=0)
V = np.append(V ,V3,axis=0)
V = np.append(V ,V4,axis=0)
#endregion

#region Compute the covariance matrix.
# Center the data by computing the mean.
Vmean = np.mean(V,axis=0)
Vcentered = V-Vmean
S = np.matmul(Vcentered.transpose(),Vcentered)
#endregion

#region Find the eigenvalues and eigenvectors of normalized correlation matrix.
EigenValues, EigenVectors = np.linalg.eigh(S)
#endregion

#region Print report.
for d in range(D):
    print("lambda%1d = %8.2f  (%6.4f) ---->  U%1d = %s"%(d, EigenValues[d],EigenValues[d]/EigenValues.max() , d, EigenVectors[d]))
if EigenValues[0]>EigenValues[1]:
    print('u0 is the principal Vector.')
    PVtoken='u0'
else:
    print('u1 is the principal Vector.')
    PVtoken = '$u_1$'
Relative_Variance = np.round(EigenValues/EigenValues.sum(),2)
#endregion

#region Plot the two principal component vectors with the centered data (within a set window range).
fig=plt.figure()
plt.subplot(121)
x,y=zip(*Vcentered)
plt.plot(x,y,'.')
plt.quiver([0,0],[0,0],[0,1],[1,0],scale_units='xy',scale=1,color='b') # Centered data axes.
plt.quiver([0,0],[0,0],EigenVectors[:,0],EigenVectors[:,1],scale_units='xy',scale=1,color='r') # Both eigenvectors.
plt.text(EigenVectors[0,0],1.2*EigenVectors[0,1],'$u_0$\n%4.2f'%EigenValues[0],horizontalalignment='center',verticalalignment='center') # First eigenvalue.
plt.text(EigenVectors[1,0],1.2*EigenVectors[1,1],'$u_1$\n%4.2f'%EigenValues[1],horizontalalignment='center',verticalalignment='center') # Second eigenvalue.
plt.xlabel('$x_0$')
plt.ylabel('$x_1$')
plt.axis('equal')
plt.axis([-1.5,1.5,-1.5,1.5])
plt.title('Eigenvectors with Maximum Variance\n(on Centered Data)',horizontalalignment='center')
#endregion

#region Project the data along each axis for comparison.
u1 = [np.dot(EigenVectors[0],Vcentered[n]) for n in range(Vcentered.shape[0]) ]
u2 = [np.dot(EigenVectors[1],Vcentered[n]) for n in range(Vcentered.shape[0]) ]
plt.subplot(122)
plt.plot(0*np.ones(len(u1)),u1,'r.')
plt.plot(1*np.ones(len(u2)),u2,'g.')
plt.xticks([0,1],['$u_0 (%4.2f)$'%Relative_Variance[0], '$u_1 (%4.2f)$'%Relative_Variance[1]])
plt.title('Projected Data\nPrincipal axis: %s'%PVtoken)
plt.show()
#endregion




