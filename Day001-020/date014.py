#函数的应用实战
#生成随机验证码
import random
import string
ALL_CHARS = string.digits + string.ascii_letters
def generate_code(code_len = 4,/):
    return ' '.join(random.choices(ALL_CHARS,k =code_len))
for _ in range(5):
    print(generate_code(6))
#判断素数
def is_prime(num:int) -> bool:
    for i in range(2,int(num**0.5+1)):
        if num % i == 0:
            return False
    return True
print(is_prime(12))
#最大公约和最小公倍数
def lcm(x:int, y:int) -> int:
    return x * y // gcb(x,y)
def gcb(x:int, y:int) -> int:
    while y % x != 0:
        x, y = y % x, x
    return x
print(lcm(2,5))
#数据统计
    #极差
def ptp(data):
    return max(data) - min(data)
    #算术平均值
def mean(data):
    return sum(data)/len(data)
    #中位数
def median(data):
    temp, size = sorted(data), len(data)
    if size % 2 != 0:
        return temp[size // 2]
    else:
        return mean(temp[size // 2 - 1 : size // 2 + 1])
    #方差(doof在这里边能够调整值，从而让计算更灵活）
def var(data, ddof=1):
    x_bar =mean(data)
    temp = [(num - x_bar)**2 for num in data]
    return sum(temp) / (len(temp)-ddof)
    #标准差
def std(data, ddof=1):
    return var(data,ddof)**0.5
print(var(data=list(range(5))))     #2.5
    #变异系数
def cv(data,ddof=1):
    return std(data,ddof) / mean(data)
    #输出描述性统计信息
def describe(data):
    print(f'均值:{mean(data)}')
    print(f'中位数:{median(data)}')
    print(f'极差:{ptp(data)}')
    print(f'方差:{var(data)}')
    print(f'标准差:{std(data)}')
    print(f'变异系数:{cv(data)}')
#双色球随机选号
import random
red_balls = [i for i in range(1,34)]
blue_balls = [i for i in range(1,17)]
def choose():
    select_balls = random.sample(red_balls,6)
    select_balls.sort()
    select_balls.append(random.choice(blue_balls))
    return select_balls
def display(balls):
    for ball in balls[:-1]:
        print(f'\033[031m{ball:0>2d}\033[0m',end='\t')
    print(f'\033[034m{balls[-1]:0>2d}\033[0m',end='\t')
n = int(input('生成几注号码：'))
for _ in range(n):
    display(choose())
