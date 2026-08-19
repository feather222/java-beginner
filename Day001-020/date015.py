#高阶函数
def calc(*args,**kwargs):
    items = list(args)+list(kwargs.values())
    result = 0
    for item in items:
        if type(item) in (int,float):
            result += item
    return result
def calc(init_value,op_func,*args,**kwargs):
    items = list(args)+list(kwargs.values())
    result = init_value
    for item in items:
        if type(item) in (int, float):
            result = op_func(result,item)
    return result
def add(x,y):
    return x+y
def mul(x,y):
    return x*y
print(calc(0,add,1,2,3,4,5))
print(calc(1,mul,1,2,3,4,5,a=0.5))

import operator
print(calc(0,operator.add,1,2,3,4,5))
#fliter,map
def is_even(num):
    return num % 2 == 0
def square(num):
    return num**2
old_nums = [35,12,8,99,60,52]
new_nums = list(map(square,filter(is_even,old_nums)))
print(new_nums)
# sorted函数
old_strings = ['in','apple','zoo','waxberry','pear']
new_strings = sorted(old_strings,key=len)
print(new_strings)  #['in', 'zoo', 'pear', 'apple', 'waxberry']
#lambda函数
old_nums = [35,12,8,99,60,52]
new_nums = list(map(lambda x: x**2,filter(lambda x:x % 2 == 0,old_nums)))
print(new_nums)
#一行实现功能
import  functools
import operator
fac = lambda n: functools.reduce(operator.mul,range(1,n+1),1)
is_prime = lambda x : all(map(lambda f: x % f == 0 , range(2,int(x**0.5)+1)))
print(fac(6))
print(is_prime(14))
#偏函数
import functools
int2 = functools.partial(int,base=2)
int8 = functools.partial(int,base=8)
int16 = functools.partial(int,base=16)
print(int('1111'))      #1111
print(int2('1111'))     #15
print(int8('1111'))     #585
print(int16('1111'))    #4369
