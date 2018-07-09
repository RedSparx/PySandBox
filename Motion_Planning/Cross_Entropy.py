'''
CROSS-ENTROPY DEMONSTRATION
---------------------------
This program measures the amount of information in two random variables, one gaussian, and the other uniform.  The
entropy is measured for each and the number of bits required to represent each (given a quantization level).  Given
codes to represent each separate random variable, the Kullback-Leibler distance is used to determine the uncertainty
that is added if we used a code for one random variable to represent another.

John Salik
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import sankey
#region Define distributions as well as the Kullback-Leibler distance.
Norm=lambda x,mu,sigma: 1/np.sqrt(2.0*np.pi*sigma**2) * np.exp(-(x-mu)**2 / (2.0*sigma**2))
Uniform = lambda x: 1/np.sum(x)
Dkl=lambda p,q: np.sum(p*np.log2(p/q))
#endregion

#region Create discrete probability distributions to work with.
N=256              # Number of discrete samples.
x=np.linspace(-5,5,N)
p=Norm(x, 0, 1)     # Sampled continuous distribution.
p=p/np.sum(p)       # Normalization.  The sum of the discrete probability distribution should be one.
# q=Norm(x, 0.5, 0.2)     # Sampled continuous distribution.
q=1/N * np.ones(N)     # Sampled continuous distribution.
q=q/np.sum(q)       # Normalization.  The sum of the discrete probability distribution should be one.
#endregion

#region Compute entropies for each distribution (in bits).
Entropy = lambda z: -np.sum(z*np.log2(z))
Hp = Entropy(p)
Hq = Entropy(q)
#endregion

#region Compute the KL distance from p->q and q->p.
Dkl_pq = Dkl(p,q)
Dkl_qp = Dkl(q,p)
#endregion

#region Compute entropy of one distribution using the code of the other.
Hp_new = Hq + Dkl_qp
Hq_new = Hp + Dkl_pq
print('Entropy H(p)\t\tEntropy H(q)\t\tDkl(p,q)\t\tDkl(q,p)')
print('%6.4f\t\t\t\t%6.4f\t\t\t\t%6.4f\t\t\t%6.4f\n\n'%(Hp,Hq,Dkl_pq,Dkl_qp))

Hpq1=Hp + Dkl_pq
Hpq2=Hq + Dkl_qp
print('Computed Cross Entropy H(p,q) = H(p)+Dkl(p,q): %6.4f'%Hpq1)
print('Computed Cross Entropy H(p,q) = H(q)+Dkl(q,p): %6.4f'%Hpq2)
#endregion

#region Display probability plots of distributions.
plt.plot(x,p,'.r',label='p(x)')
plt.plot(x,q,'.b',label='q(x)')
plt.legend()
#endregion

#region Display Sankey plot of computations.
S1 = sankey.Sankey()
S1.add(flows=[-Hpq1,Hp,Dkl_pq],
       orientations=[0,0,1],
       labels=['H(p,q)','H(p)','D(p,q)'],
       pathlengths=[5,1,3])
S1.finish()
plt.title('Code for p(x), Samples From q(x)')
S2 = sankey.Sankey()
S2.add(flows=[-Hpq2,Hq,Dkl_qp],
       orientations=[0,0,1],
       labels=['H(p,q)','H(q)','D(q,p)'],
       pathlengths=[5,1,3])
S2.finish()
plt.title('Code for q(x), Samples From p(x)')
plt.show()
#endregion
