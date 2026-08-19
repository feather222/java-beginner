#创建集合
set1 = {1,2,3,3,2,1}
print(set1)
set2 = {'banana','pitaya','apple','banana','grape'}
print(set2)
set3 = set('hello')
print(set3)
set4 = set([1,2,2,3,3,3,2,1])
print(set4)
set5 = {num for num in range(1,20) if num % 3 == 0 or num % 7 == 0 }
print(set5)
"""
{1, 2, 3}
{'grape', 'pitaya', 'apple', 'banana'}
{'h', 'l', 'o', 'e'}
{1, 2, 3}
{3, 6, 7, 9, 12, 14, 15, 18}
"""
set1 = {'python', 'c++', 'java', 'kotlin', 'swift'}
for elem in set1:
    print(elem)
#集合的运算
    #成员运算
print('banana' in set2)
print(3 in set1)
    #对称运算
set1 = {i for i in range(1,8)}
set2 = {i for i in range(11) if i % 2 == 0}
    #交集
print(set1 & set2)
print(set1.intersection(set2))      #{2, 4, 6}
    #并集
print(set1 | set2)
print(set1.union(set2))             #{0, 1, 2, 3, 4, 5, 6, 7, 8, 10}
    #差集
print(set1 - set2)
print(set1.difference(set2))
    #对称差
print(set1 ^ set2)
print(set1.symmetric_difference(set2))  #{0, 1, 2, 3, 4, 5, 6, 7, 8, 10}
set1 = {1,3,5,7}
set2 = {2,4,6}
set1 |= set2
# set1.update(set2)
print(set1)     #{1, 2, 3, 4, 5, 6, 7}
set3 = {3,6,9}
set1 &= set3
# set1.intersection_update{set3}
print(set1)     #{3, 6}
set2 -= set1
# set2.difference_update(set1)
print(set2)     #{2, 4}
    #比较运算：set1 < set2判断set1是不是set2的真子集，set1 <= set2判断set1是不是set2的子集，set2 > set1判断set2是不是set1的超集
set1 = {1,3,5}
set2 = {i for i in range(1,6)}
set3 = {i for i in range(5,0,-1)}
print(set1 < set2)      #True
print(set1 <= set2)     #True
print(set2 < set3)      #Falsh
print(set2 <= set3)     #True
print(set2 > set1)      #True
print(set2 == set3)     #True
print(set1.issubset(set2))      #True
print(set2.issuperset(set1))    #True
#集合的方法
    #添加元素
set1 = {1,10,100}
set1.add(1000)
set1.add(10000)
print(set1)     #{1, 100, 1000, 10, 10000}
    #删除元素
set1.discard(10)
if 100 in set1:
    set1.remove(100)
print(set1)     #{1, 1000, 10000}
    #清空元素
set1.clear()
print(set1)     #set()
    #判断两个集合是否有相同元素,没有相同元素返回True
set2 = {'java','python','c++','kotlin'}
set3 = {'kotlin','swift','java','dart'}
print(set2.isdisjoint(set3))        #False
#不可变集合
fset1 = frozenset({1,3,5,7})
fset2 = frozenset(range(1,6))
print(fset1)            #frozenset({1, 3, 5, 7})
print(fset1 & fset2)    #frozenset({1, 3, 5})
print(fset1 | fset2)    #frozenset({1, 2, 3, 4, 5, 7})
print(fset1 - fset2)    #frozenset({7})
print(fset1 < fset2)    #False
