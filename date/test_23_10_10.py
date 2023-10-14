""" a=input()
b=a.split()
c=[int(x) for x in b]
print(c) """

""" a=input()
b=a.split()
i=0
for x in b:
    b[i]=int(x)
    i+=1
print(b) """

""" a=input().split()
print(a) """

""" name = ['Niumei', 'YOLO', 'Niu Ke Le', 'Mona']
food=['pizza', 'fish', 'potato', 'beef']
number=[3, 6, 0, 3]
friends=[]
friends.append(name)
friends.append(food)
friends.append(number) """

""" a=char(input().split())
print(a) """

a=str(1012)
print(a[::-1])

import math
huiwen=[]
for x in range(0,10):
    huiwen.append(x)
for x in range(10,100):
    if (x%10)==math.floor(x/10):
        huiwen.append(x)
print(huiwen)