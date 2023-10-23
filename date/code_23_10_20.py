#leetcode 算法 202 快乐数
""" 编写一个算法来判断一个数 n 是不是快乐数。
「快乐数」 定义为：
对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果这个过程 结果为 1，那么这个数就是快乐数。
如果 n 是 快乐数 就返回 true ；不是，则返回 false 。 """

def happy_number(num):
    if num>=100:
        return int(num/100)**2+int(int(num%100)/10)**2+(num%10)**2
    elif num>=10:
        return int(num/10)**2+(num%10)**2
    else:
        return num**2


n=int(input('n = '))
count=0
while count<10000:
    n=happy_number(n)
    if n==1:
        print('ture')
        break
    count+=1
if count==10000:
    print('false')
