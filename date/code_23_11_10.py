
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
n=20
p=0.2
x=np.arange(0,21,1)
y_pmf=stats.binom.pmf(x,n,p)
y_cdf=stats.binom.cdf(x,n,p)
plt.bar(x,y_pmf)
plt.plot(x,y_cdf,color='red')
plt.title('Binomial Distribution:n=%i,p=%.2f'%(n,p))
plt.xlabel('n')
plt.ylabel('probalility')
plt.text(x=4.5,y=0.25,s='pmf',alpha=0.75,weight='bold',color='blue')
plt.text(x=14.5,y=0.9,s='cdf',rotation=.75,weight='bold',color='red')
plt.show()