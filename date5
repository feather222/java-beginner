#循环结构
#for-in循环
import time

for _ in range(5):
    print('Hello World')
    time.sleep(1)
    #一到一百求和
total1 = 0
for i in range ( 1 , 101 ):
        total1 += i
print(total1)
    #1-100奇数和
total2 = 0
for i in range (1,101,2):
    total2 += i
print(total2)
print(sum(range( 0 , 101 ,2)))#偶数和
#while循环
total3 = 0
i = 1
while i <= 100:
    total3 += i
    i += 1
print(total3)
    #break和continue的使用，求1-100的奇数和
total4 = 0
i = 1
while True:
    total4 += i
    i += 2
    if i > 99:
        break
print(f'求和结果是{total4}')
total5 = 0
for i in range (1,101):
    if i % 2 != 1:
        continue
    total5 += i
print(f'求和结果{total5 = }')
#嵌套循环
for i in range( 10 ):
    for j in range( 1 , i +1):
        print(f'{i}×{j}={i*j}', end = '\t')
    print()
#循环结构应用
#eg1判断素数
num = (int(input('请输入数值')))
end = int(num ** 0.5)
is_prime = True
for i in range ( 2 , end + 1):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print(f'{num}是素数')
else:
    print(f'{num}不是素数')
#最大公约数
x = int(input('请输入x的值'))
y = int(input('请输入y的值'))
while y % x != 0:
    x , y = y % x , x
print(f'最大公约数是{x}')
#猜字谜
import random
answer = random.randrange(1,10)
counter = 0
while True:
    counter += 1
    num = int(input('猜一个整数'))
    if num < answer:
        print('猜小了')
    elif num > answer:
        print('猜大了')
    else:
        print('猜对了')
        break
print(f'正确答案是{answer}，你猜了{counter}次')
