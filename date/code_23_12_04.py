import random
from math import floor

a1=random.randint(101,500)
a2=random.randint(101,500)

b=int(input("请输入你的座位号:"))
c1=floor(a1/100)+10*floor(a1%100/10)+100*(a1%10)
c2=floor(a2/100)+10*floor(a2%100/10)+100*(a2%10)
if b==a1 or b==a2:
    print("你获得一等奖")
elif b==c1 or b==c2:
    print("你获得二等奖")
elif b%10==a1%10 or b%10==a2%10:
    print("你获得三等奖")
else:
    print("感谢参与")