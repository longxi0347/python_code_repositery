#实验三源代码
""" import numpy as np
nstd=22
ntimes=1000
fre=0

for i in range(ntimes):
    s=0
    data=np.random.uniform(1,336,nstd)
    date=np.floor(data)
    date=np.array(date)
    newdate=set(date)
    nsize=len(newdate)
    if nsize<nstd:
        fre=fre+1

print(fre)
print(fre/ntimes) """

#程序1
""" import numpy as np
nstd=22
ntimes=1000
fre=0

for i in range(ntimes):
    date=[]
    for x in range(nstd):
        date.append(np.random.randint(1,366))
    newdate=set(date)
    nsize=len(newdate)
    if nsize<nstd:
        fre=fre+1

print(fre)
print(fre/ntimes) """

#程序2
import numpy as np

times=100000
res_1=0
res_2=0

for x in range(times):
    a=np.random.randint(1,7)
    b=np.random.randint(1,7)
    c=a+b
    if c==7:
        res_1+=1
        if a==1 or b==1:
            res_2+=1

print("和为7的概率：%.2f"%(res_1/times))
print("当和为7时，有一个为1的概率：%.2f"%(res_2/res_1))

