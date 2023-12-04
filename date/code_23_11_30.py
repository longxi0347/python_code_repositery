#第一题 在同一坐标系内绘出参数为0.5, 1, 3的指数分布的概率密度曲线。
#要求：
#横坐标限定为0到5
#纵坐标限定为0到3
#=0.5的曲线用蓝色实线
#=1的曲线用绿色虚线
#=3的曲线用黑色点虚线

""" import numpy as np  
import matplotlib.pyplot as plt  
from scipy.stats import expon  

x=np.linspace(0, 10, 1000)
y1=expon.pdf(x,scale=1/0.5)
y2=expon.pdf(x,scale=1/1)
y3=expon.pdf(x,scale=1/3)

plt.figure(figsize=(10, 6))  


plt.plot(x, y1, label=f'λ = 0.5', linestyle='-', color='b')  
plt.plot(x, y2, label=f'λ = 1.0', linestyle='--', color='g')  
plt.plot(x, y3, label=f'λ = 3.0', linestyle=':', color='k')  


plt.xlim([0, 5]) 
plt.ylim([0, 3])  
plt.legend()  
plt.show() """

#第二题 补完实验2的程序:分别产生服从N(mu,sig1^2)和N(mu,sig2^2)的两组随机数，每组N个，
#统计每组随机数落入[mu-a,mu+a]和[mu-2a,mu+2a]两个区间内的频率。其中mu=3, sig1=1, sig2=2, N=2000, a=1, 实验2原程序中画图部分可省略。

""" import numpy as np  
import matplotlib.pyplot as plt  

mu = 3
sig1 = 1 
sig2 = 2

n = 2000  
data1 = np.random.normal(mu, sig1, n) 
data2 = np.random.normal(mu, sig2, n) 

interval1 = np.logical_and(mu-1 <= data1, data1 <= mu+1)  
interval2 = np.logical_and(mu-2 <= data1, data1 <= mu+2)  
interval3 = np.logical_and(mu-1 <= data2, data2 <= mu+1)  
interval4 = np.logical_and(mu-2 <= data2, data2 <= mu+2)

freq1 = np.sum(interval1) / n  
freq2 = np.sum(interval2) / n  
freq3 = np.sum(interval3) / n  
freq4 = np.sum(interval4) / n 

print(f"sig1=1,落在[μ-a,μ+a]的频率：{freq1:.4f}")  
print(f"sig1=1,落在[μ-2a,μ+2a]的频率：{freq2:.4f}") 
print(f"sig2=2,落在[μ-a,μ+a]的频率：{freq3:.4f}") 
print(f"sig2=2,落在[μ-2a,μ+2a]的频率：{freq4:.4f}")  """

#第三题 程序模拟：10个球，三个0号，三个1号，两个2号，两个3号。每次随机取一个，有放回，取3次，X是3个号码的和，求X在1000次模拟中的平均值(期望)。
#考虑到这个问题可能有一定难度，可以参考学习通上的4-c1.py，这是对每次取一个球的情况做模拟。一次取三个球的模拟方法是完全类似的。

""" import random  

balls = [0]*3 + [1]*3 + [2]*2 + [3]*2  

num_simulations = 1000  
total_sum = 0  

for _ in range(num_simulations):  
    for x in range(3):
        ball = random.choice(balls)   
        total_sum += ball  

average_sum = total_sum / num_simulations  
print("平均值（期望）为：", average_sum) """