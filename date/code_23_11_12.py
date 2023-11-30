# 1（2）固定p=0.2，分别取n=10,20,50，在同一坐标系内绘出二项分布的概率分布图，图中将顶点按顺序连成折线，称为概率分布曲线。
# 要求：n=10的曲线用蓝色，圆形和实线
# n=20的曲线用绿色，方形和虚线
# n=50的曲线用黑色，星形和点虚线，为了美观，图中只取n<=20的部分

""" import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

n1=10
n2=20
n3=50
p=0.2

x1=np.arange(0,11,1)
x2=np.arange(0,21,1)
x3=np.arange(0,51,1)

y_pmf1=stats.binom.pmf(x1,n1,p)
y_pmf2=stats.binom.pmf(x2,n2,p)
y_pmf3=stats.binom.pmf(x3,n3,p)

plt.xlim(right=20)

plt.plot(x1,y_pmf1,'.',color='blue',linestyle='-')
plt.plot(x2,y_pmf2,'.',color='green',linestyle='--')
plt.plot(x3,y_pmf3,'*',color='black',linestyle='-.')
plt.title('Binomial Distribution:n=20,p=%.2f'%(p))

plt.xlabel('n')
plt.ylabel('probalility')
plt.show() """

# 1（5）（6）在同一坐标系下画出二项分布与泊松分布的概率分布曲线；固定np不变，增大n，减小p，观察二项分布图形的变化。
# 要求：固定np=4，让用户输入n
# 二项分布的曲线用红色圆形实线
# 泊松分布的曲线用黑色三角形虚线，图中只取0到n的部分

""" import numpy
import scipy.stats as stats
import matplotlib.pyplot as plt

np=4
n=int(input("请输入n:"))
x=numpy.arange(0,n+1)
p=np/n

plt.plot(x,stats.binom.pmf(x,n,p),'o',color='red',linestyle='-')
plt.plot(x,stats.poisson.pmf(x,np),'^',color='black',linestyle='--')

plt.show() """

# 2（4）自选μ和σ^2，产生n个服从正态分布的随机数，分别统计落入[μ-σ,μ+σ]，[μ-2σ,μ+2σ]，[μ-3σ,μ+3σ]内的频率。

""" import numpy as np  
import matplotlib.pyplot as plt  

mu = 0  
sigma = 1  

n = 10000  
data = np.random.normal(mu, sigma, n)  

interval1 = np.logical_and(mu-sigma <= data, data <= mu+sigma)  
interval2 = np.logical_and(mu-2*sigma <= data, data <= mu+2*sigma)  
interval3 = np.logical_and(mu-3*sigma <= data, data <= mu+3*sigma)  

freq1 = np.sum(interval1) / n  
freq2 = np.sum(interval2) / n  
freq3 = np.sum(interval3) / n  

print(f"落在[μ-σ,μ+σ]的频率：{freq1:.4f}")  
print(f"落在[μ-2σ,μ+2σ]的频率：{freq2:.4f}")  
print(f"落在[μ-3σ,μ+3σ]的频率：{freq3:.4f}") """