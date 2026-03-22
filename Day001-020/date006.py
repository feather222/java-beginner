#100以内的素数
for num in range(2,100):
    is_prime = True
    for i in range (2,int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
#斐波那契数列
a , b = 0 , 1
for _ in range(20):
    a , b = b , a+b
    print(a)
#寻找水仙花数
for i in range (100 , 1000 ):
    high = i // 100
    mid  = i // 10 % 10
    low  = i % 10
    if i == high ** 3 +mid ** 3 +low ** 3:
        print(i)
#翻转数字
num = int(input ('请你输入判断数值'))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)
#百钱白鸡问题
for x in range( 1,21 ):
    for y in range( 1,34 ):
        if 5 * x + 3 * y + (100 - x - y) / 3 == 100 and (100 - x - y) %  3 == 0:
            print(f'{x}只公鸡{y}只母鸡{100 - x - y}只小鸡')
#赌博游戏
import random
money = 1000
while money > 0:
    print(f'资金剩余{money}')
    while True:
        debt = int (input('请输入下注金额'))
        if 0 < debt <= money:
            break
    first_point = random.randrange(1,7)+random.randrange(1,7)
    print(f'玩家摇出了{first_point}点')
    if first_point == 7 or first_point == 11:
        print('玩家获胜')
        money += debt
    elif first_point == 2 or first_point == 3 or first_point == 12:
        print('庄家获胜')
        money -= debt
    else:
        while True:
            current_point = random.randrange(1,7)+random.randrange(1,7)
            print(f'当前点数是{current_point}')
            if current_point == 7:
                print('庄家获胜')
                money -= debt
                break
            elif current_point == first_point:
                print('玩家获胜')
                money += debt
                break
print('你已破产，游戏结束')
