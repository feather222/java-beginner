#函数和模块
def fac(num):
    result = 1
    for n in range(2,num+1):
        result *= n
    return result
m = int(input('m='))
n = int(input('n='))
print(fac(m)//fac(n)//fac(m-n))
    #math模块简化
from math import factorial
m = int(input('m ='))
n = int(input('n ='))
print(factorial(m)//factorial(n)//factorial(m-n))
    #as关键词简化
from math import factorial as f
m = int(input('输入m的值：'))
n = int(input('输入n的值：'))
print(f(m)//f(n)//f(m-n))
#函数的参数
def make_judement(a,b,c):
    return a + b > c and b + c > a and a + c > b
print(make_judement(b=1,a=2,c=3))
    #强制位置参数(强制位置参数，不允许给参数名称）
def make_judement(a,b,c,/):
    return a + b > c and a + c > b and b + c > a
print(make_judement(1,2,3))
    #*强制关键字参数
def make_judement(*,a,b,c ):
    return a + b > c and a + c > b and b + c > a
print(make_judement(a=1, b=2, c=3))
    #参数的默认值(带默认值的参数必须放在不带默认值的参数之后)
def add(a=0,b=0,c=0):
    return a + b + c
print(add())                    #0
print(add(1,2))           #3
print(add(1,2,3))      #6
    #可变参数(*可引入多个普通参数，**可引入多个关键词参数）
def add(*args):
    total = 0
    for val in args:
        if type(val) in (int, float):
            total += val
    return total
print(add(1,2,1.5,1.5,'hello world'))       #6.0
def foo(*args, **kwargs):
    print(args)
    print(kwargs)
    foo(1,2,3,name = '林志颖', age = 25)
"""
(1, 2, 3)
{'name': 'lzy', 'age': 25}
"""
#用模块管理函数
from module.module1 import foo as f1
from module.module2 import foo as f2
f1()    #hello world
f2()    #goodbye world
