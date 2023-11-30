import random

lis=['凤毛麟角','釜底抽薪','耳濡目染','鬼斧神工','海市蜃楼','囫囵吞枣','墨守成规','事倍功半','殊途同归','脱颖而出','无与伦比','作茧自缚','杯弓蛇影','鳞次栉比','三人成虎','一言九鼎']
#16个成语
point=20
for i in range(1,9):
    a=random.randint(0,15)
    b=lis[a]
    c=random.randint(0,3)
    d=list(b)
    e=d[c]
    d[c]='_'
    print(d[0],d[1],d[2],d[3])
    f=input("请输入答案:")
    if f==e:
        print("正确")
        point+=2
    elif f=='':
        continue
    elif f!=e:
        print("错误")
        point-=2
print(point)