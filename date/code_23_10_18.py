#有n个人排队，求甲和乙相邻的概率
""" import random

n=int(input())
list=[x for x in range(1,n-1)]
list.append('甲')
list.append('乙')
answer=0

for x in range(100000):
    random.shuffle(list)
    if list.index('甲')-list.index('乙')==1 or list.index('乙')-list.index('甲')==1:
        answer+=1

print(answer/100000) """

a={'<': 'less than','==': 'equal'}
print('Here is the original dict:')
for x,y in sorted(a.items()):
    print(f'Operator {x} means {y} than.')
a['>']='greater than'
print=()
print('The dict was changed to:')
""" for d,j in sorted(a.items()):
    print(f'Operator {d} means {j}.') """