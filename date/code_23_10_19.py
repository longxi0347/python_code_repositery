#通过ASCII码打印字符
""" a=65
print("%c"%(a)) """

char=input()
i=0
list=[x for x in range(65,91)]
#找到输入字符在列表中的位置
for x in list:
    if chr(x)==char:
        break
    i+=1

for x in range(i+1):
    print('-'*(i-x),end='')
    y=x
    for m in range(x+1):
        print("%c"%(m+65),end='')
    
    while y>=1:
        print("%c"%(y+64),end='')
        y-=1

    print('-'*(i-x))
