import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.integrate import simps

#region Generate the normal probability density function (pdf) with a compact support region.
x=np.linspace(-10,10,1000)
f=lambda x: norm.pdf(x)
#endregion

#region Print analytic results.
# Verify that the function is in fact a density function by integrating it over the support region.  Then, compute the
# differential entropy and display the result.  Recall that the differential (continuous) entropy is defined as
# follows:                   /
#                     h(X) = | f(x) log f(x) dx
#                            /
#                            X
#
PDF_Integration=simps(f(x),x)
Differential_Entropy_bits=-simps(f(x)*np.log2(f(x)),x)
Theoretical_Differential_Entropy_bits=0.5*np.log2(2*np.pi*np.e)
Differential_Entropy_nats=-simps(f(x)*np.log(f(x)),x)
Theoretical_Differential_Entropy_nats=0.5*np.log(2*np.pi*np.e)
print('PDF Integration:\t\t%2.4f'%PDF_Integration)
print('Differential Entropy:\t%2.4f bits or %2.4f nats'%\
      (Differential_Entropy_bits,Differential_Entropy_nats))
print('Theoretical Value:\t\t%2.4f bits or %2.4f nats'%\
      (Theoretical_Differential_Entropy_bits,Theoretical_Differential_Entropy_nats))

#endregion

#region Plot the density function and save it.
plt.plot(x,f(x))
plt.title('Normal Distribution: h(X)=%2.4f nats'%Differential_Entropy_nats)
plt.ylabel('$f(x)$')
plt.xlabel('$x$')
plt.show()
plt.savefig('Gaussian_Differential_Entropy.png')
#endregion