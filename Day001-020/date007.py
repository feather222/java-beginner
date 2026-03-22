#创建列表
items1 = ['c','java','python','C++','C#']
items2 =list(range(5))
print(items2)
print(type(items1))
"""
[0, 1, 2, 3, 4]
<class 'list'>
"""
#列表的运算
print(items1 + items2)
print(items1 * 3)
print( 2 in items2 )
print('java' not in items1)
"""
['c', 'java', 'python', 'C++', 'C#', 0, 1, 2, 3, 4]
['c', 'java', 'python', 'C++', 'C#', 'c', 'java', 'python', 'C++', 'C#', 'c', 'java', 'python', 'C++', 'C#']
True
False
"""
    #列表指定范围为0——N-1或者-1——-N
print(items1[2])
print(items1[-3])
print(items2[-1:-4:-2])
print(items1[2:4:1])
print(items1[::])
"""
python
python
[4, 2]
['python', 'C++']
['c', 'java', 'python', 'C++', 'C#']
"""
   #list插入
items1[1:3] = ['watermelon' , 'peach']
print(items1)
nums3 = [1, 2, 3, 4]
nums4 = list(range(1, 5))
nums5 = [3, 2, 1]
print(nums3 == nums4) #True
print(nums4 >= nums5) #False
#元素的遍历
languages = ['python','java','c++','kotlin']
for index in range (len(languages)):
    print(languages[index])
for language in languages:
    print(language)
"""
python
java
c++
kotlin
"""
#投骰子，点数对应次数
import random
counters = [0] * 6
for _ in range(6000):
    face = random.randrange (1,7)
    counters[face-1] += 1 #[face-1]是元素位置
for face in range(1,7): #设定点数
    print(f'{face}点出现了{counters[face-1]}次')
