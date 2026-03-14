#列表添加和删除元素
    #添加
languages = ['Pyhton','Java','C++']
languages.append('javascrpt')
print(languages) #['pyhton', 'java', 'c++', 'javascrpt']
languages.insert(1,'SQL')
print(languages) #['pyhton', 'SQL', 'java', 'c++', 'javascrpt']
    #删除
languages = ['python','SQL','java','c++','javascrpt']
if 'java' in languages:
    languages.remove('java')
if 'swift' in languages:
    languages.remove('swift')
print(languages) #['python', 'SQL', 'c++', 'javascrpt']
languages.pop()
temp = languages.pop(1)
print(temp) #SQL
languages.append(temp)
print(languages)    #['python', 'c++', 'SQL']
languages.clear()
print(languages)    #[]
languages = ['python','SQL','java','c++','javascrpt','python']
languages.remove('python')
print(languages)    #['SQL', 'java', 'c++', 'javascrpt', 'python']
    #元素的位置和频次
items = ['python','java','java','c++','kotlin','python']
print(items.index('python'))    #默认第0位元素
print(items.index('python',1))
print(items.count('python'))
print(items.count('kotlin'))
print(items.count('swift'))
print(items.index('java',3))
""" 0   5   2   1   0   'java' is not in list   """
    #元素排序和翻转
items = ['python','java','c++','kotlin','swift']
items.sort()
print(items)    #['c++', 'java', 'kotlin', 'python', 'swift']
items.reverse()
print(items)    #['swift', 'python', 'kotlin', 'java', 'c++']
#列表生成式
    #场景一：创建一个取值范围在1到99且能被3或者5整除的数字构成的列表。
items=[]
for i in range(1,100):
    if i % 3 == 0 or i % 5 == 0:
        items.append(i)
print(items)

items = [ i  for i in range(1,100) if i % 3 == 0 or i % 5 == 0]
print(items)
    #场景二：有一个整数列表nums1，创建一个新的列表nums2，nums2中的元素是nums1中对应元素的平方。
nums1 = [ 22,33,44,55 ]
nums2 = []
for num in nums1:
        nums2.append(num**2)
print(nums2)

nums1 = [22,33,44,55]
nums2 = [num**2 for num in nums1]
print(nums2)
    #场景三： 有一个整数列表nums1，创建一个新的列表nums2，将nums1中大于50的元素放到nums2中。
nums1 = [11,22,33,44,55,66,77,88,99]
nums2 = []
for num in nums1:
    if num > 50 :
        nums2.append(num)
print(nums2)

nums2 = [num for num in nums1 if num > 50]
print(nums2)
#嵌套列表
scores = [[95,83,92],[80,75,82],[92,97,90],[80,78,69],[65,66,89]]
print(scores[0])
print(scores[1][2])
    #五名学生的三门课成绩录入
scores = []
for _ in range(5):
    temp = []
    for _ in range(3):
        score = int(input('请输入成绩'))
        temp.append(score)
    scores.append(temp)
print(scores)

import random
scores = [[random.randrange(60,101) for _ in range(3) ] for _ in range(5)]
print(scores)
#列表的应用
    #双色球
import random
red_balls = list(range(1,34))
select_balls = []
for _ in range(6):
    index = random.randrange(len(red_balls))
    select_balls.append(red_balls.pop(index))
select_balls.sort()
for ball in select_balls:
    print(f'\033[031m{ball:0>2d}\033[0m',end=' ')
blue_ball = random.randrange(1,17)
print(f'\033[034m{blue_ball:0>2d}\033[0m')
    #sample（无放回随机抽取）和choice（随机抽一个）简化
import random
red_balls = [i for i in range(1,34)]
blue_balls = [i for i in range(1,17)]
select_balls = random.sample(red_balls,6)
select_balls.sort()
for select_ball in select_balls:
    print(f'\033[031m{select_ball}\033[0m',end = ' ')
blue_ball = random.choice(blue_balls)
print(f'\033[034m{blue_ball}\033[0m')
#执行N次
import random
n = int(input('请输入生成组数'))
red_balls = [i for i in range(1, 34)]
blue_balls = [i for i in range(1, 17)]
for _ in range(n):
    select_balls = random.sample(red_balls, 6)
    select_balls.sort()
    for select_ball in select_balls:
        print(f'\033[031m{select_ball:0>2d}\033[0m', end=' ')
    blue_ball = random.choice(blue_balls)
    print(f'\033[034m{blue_ball:0>2d}\033[0m')
    #rich第三方库
import random
from rich.console import Console
from rich.table import Table
console = Console() #创建控制台
n = int(input('输入组数'))
red_balls = [i for i in range(1,34)]
blue_balls = [i for i in range(1,17)]
    #创建表头
table = Table(show_header = True)
for col_name in ('序号','红球','蓝球'):
    table.add_column(col_name,justify = 'center')
for i in range(n):
    select_balls = random.sample(red_balls,6)
    select_balls.sort()
    blue_ball = random.choice(blue_balls)
    #添加行
    table.add_row(
        str(i+1),
        f'[red]{" ".join([f"{ball:0>2d}" for ball in select_balls])}[/red]',
        f'[blue]{blue_ball:0>2d} [/blue]'
    )
console.print(table)
