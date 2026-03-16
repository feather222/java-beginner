#元组的定义和运算
t1 = (35,12,98)
t2 = ('名字',45,True,'地址')
print(type(t1)) #<class 'tuple'>
print(len(t2))  #45
print(t2[-1])   #地址
    #切片运算
print(t2[:2])   #('名字', 45)
print(t2[::3])  #('名字', '地址')
    #元素遍历
for elem in t1:
    print(elem)
print(11 in t1) #False
print('hao' not in t2)  #True
t3 = t1 + t2
print(t3)   #(35, 12, 98, '名字', 45, True, '地址')
print(t1 == t2)             #False
print(t1 >= t3)             #False
print(t1 <= (35,11,99))     #False
d = ('hello',)
print(type(d))      #<class 'tuple'>
#打包和解包操作
    #打包操作
a = 1,10,100
print(type(a))  #<class 'tuple'>
print(len(a))   #3
print(a)        #(1, 10, 100)
    #解包操作
i , j , k = a
print(i , j , k)    #1 10 100
a = 1, 10, 100, 1000
i , j , *k = a
print(i, j, k)              #1 10 [100, 1000]
i , j , k , l , *m = a
print(i , j , k , l , m)    #1 10 100 1000 []
a, b, *c = range(1, 10)
print(a, b, c)       #1 2 [3, 4, 5, 6, 7, 8, 9]
a, b, c = [1, 10, 100]
print(a, b, c)       #1 10 100
a, *b, c = 'hello'
print(a, b, c)      #h ['e', 'l', 'l'] o
#交换变量的值
a, b = b, a
a, b, c = b, c, a
"""不可变类型更适合多线程环境
不可变类型在创建时间上优于对应的可变类型"""
import timeit

print('%.3f 秒' % timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]', number=10000000))
print('%.3f 秒' % timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)', number=10000000))
#元组和列表类型是可以相互转换的
infos = ('羽毛' , 45 , True , '四川成都')
print(list(infos))      #['羽毛', 45, True, '四川成都']
frts = ['apple' , 'banana' , 'orange']
print(tuple(frts))      #('apple', 'banana', 'orange')
