#用python实现矩阵及其运算

""" from sympy import*       #从sympy中导出所有函数
init_printing(use_unicode=True)
A=Matrix([[1,5,-1,-1],[1,-2,1,3],[3,8,-1,1],[1,-9,3,7]])
print("矩阵的行数与列数:",A.shape)
print("矩阵的转置:",A.T)
print("矩阵的行简化阶梯矩阵:\n",A.rref())
print("矩阵的秩:",A.rank())
print("矩阵的逆矩阵:",A**(-1)) """

""" #实验训练1
from sympy import*
A=Matrix([[1,2,3],[2,1,2],[3,3,1]])
B=Matrix([[3,2,4],[2,5,3],[2,3,1]])
print("2A-B:",2*A-B,"\nAB:",A*B,"\nBA:",B*A,"\nA^TB:",A.T*B)
print("A的阶梯型矩阵:\n",A.rref())
print("B的逆矩阵:",B**(-1))
print("B的秩:",B.rank()) """

""" #实验训练2
from sympy import*
A=Matrix([[4,2,3],[1,1,0],[-1,2,3]])
E=Matrix([[1,0,0],[0,1,0],[0,0,1]])
print("B=",A*(A-2*E)**(-1)*A) """

from sympy import*
a=symbols('a')
A=Matrix([[1+a,1,1,1,1],[1,1+a,1,1,1],[1,1,1+a,1,1],[1,1,1,1+a,1],[1,1,1,1,1+a]])
print("逆矩阵:\n",A**(-1))