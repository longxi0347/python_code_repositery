""" def f(n):
    if n==1 or n==0:
        return 1
    return n*f(n-1)

print(f(12)) """

""" def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        result=1
        while n:
            result=result*n
            n-=1
    return result

a=int(input())
b=factorial(a)
print(b) """

""" a=int(input())
while a:
    print('*'*a)
    a-=1  """

""" def ff(n):
    print('*'*n)
    n-=1
    if n>0:
        ff(n)

n=int(input())
ff(n) """

def f(n):
    if n==1:
        print("*")
    else:
        print("*"*n)
        f(n-1)

a=int(input())
f(a)