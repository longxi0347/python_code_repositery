#牛客网 NP48--NP60
#牛客网 NP48 验证登录名与密码
""" name='admis'
password='Nowcoder666'
a=input()
b=input()
if a==name and b==password:
    print("Welcome!")
else:
    print("user id or password is not correct!") """

#牛客网 NP49 字符列表的长度
""" my_list=['P','y','t','h','o','n']
print("Here is the original list:")
print(my_list,"\n")
print("The number that my_list has is:")
print(len(my_list)) """

#牛客网 NP50 程序员节
""" users_list=['Niuniu','Niumei','Niu Ke Le']
for x in users_list:
    print(f'Hi, {x}! Welcome to Nowcoder!')
print("Happy Programmers' Day to everyone!") """

#牛客网 NP51 列表的最大与最小
""" list=[x for x in range(10,51)]
print(list)
print(f'{list[0]} {list[-1]}') """

#牛客网 NP52 累加数与平均值
""" list=input().split()
list=[int(x) for x in list]
print("%d %.1f"%(sum(list),sum(list)/len(list))) """

#牛客网 NP53 前10个偶数
""" my_list=list(range(0,19,2))
for x in my_list:
    print(x) """

#牛客网 NP54 被5整除的数字
""" my_list=list(range(5,51,5))
for x in my_list:
    print(x) """

#牛客网 NP55 2的次方数
""" my_list=list(range(1,11))
i=0
for x in my_list:
    my_list[i]=2**x
    print(my_list[i])
    i+=1 """

#牛客网 NP56 列表解析
""" list=[x for x in range(0,10)]
print(list) """

#牛客网 NP57 格式化清单
""" list=['apple', 'ice cream', 'watermelon', 'chips', 'hotdogs', 'hotpot']
while list!=[]:
    eat=list.pop()
    print(list)
#注意列表越界访问 """

#牛客网 NP58 找到HR
""" users_list=['Niuniu','Niumei','HR','Niu Ke Le','GURR','LOLO']
for x in users_list:
    if x=='HR':
        print( 'Hi, HR! Would you like to hire someone?')
    else:
        print(f'Hi, {x}! Welcome to Nowcoder!') """

#牛客网 NP59 提前结束的循环
""" list=[3, 45, 9, 8, 12, 89, 103, 42, 54, 79]
guess=int(input())
for x in list:
    if x==guess:
        break
    else:
        print(x) """

#牛客网 NP60 跳过列表的某个元素
""" list=[x for x in range(1,16)]
for x in list:
    if x==13:
        continue
    else:
        print(x,end=' ') """