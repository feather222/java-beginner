#扑克游戏
from enum import Enum
class Suite(Enum):
    SPADE,HEART,CLUB,DIAMOND = range(4)
for suite in Suite:
    print(f'{suite}:{suite.value}')
    #定义牌类
class Card:
    def __init__(self,suite,face):
        self.suite = suite
        self.face = face
    def __repr__(self):
        suites = '♠♥♣♦'
        faces = ['','A','2','3','4','5','6','7','8','9','10','J','Q','K']
        return f'{suites[self.suite.value]}{faces[self.face]}'
    def __lt__(self, other):
        if self.suite == other.suite:
            return self.face < other.face   #同花色比较数值
        return self.suite.value < other.suite.value     #不同花色按花色代表的数值排序
    #测试喜Card
card1 = Card(Suite.SPADE,5)
card2 = Card(Suite.HEART,13)
print(card1)    #♠5
print(card2)    #♥K
    #定义扑克类
import random
class Poker:
    def __init__(self):
        self.cards = [Card(suite,face)
                      for suite in Suite
                      for face in range(1,14)]
        self.current = 0    #记录发牌位置
    def shuffle(self):
        self.current = 0
        random.shuffle(self.cards)
    def deal(self):
        card = self.cards[self.current]
        self.current += 1
        return card
    @property
    def has_next(self):
        return self.current<len(self.cards)
poker = Poker()
print(poker.cards)
poker.shuffle()
print(poker.cards)
    #定义玩家
class Player:
    def __init__(self,name):
        self.name = name
        self.cards = []
    def get_one(self,card):
        self.cards.append(card)
    def arrange(self):
        self.cards.sort()
poker = Poker()
poker.shuffle()
players = [Player('东邪'),Player('西毒'),Player('南帝'),Player('北丐')]
for _ in range(13):
    for player in players:
        player.get_one(poker.deal())
for player in players:
    player.arrange()
    print(f'{player.name}:',end=' ')
    print(player.cards)
#工资结算系统
from abc import ABCMeta,abstractmethod
class Employee(metaclass=ABCMeta):
    def __init__(self,name):
        self.name = name
    @abstractmethod
    def get_salary(self):
        pass
class Manager(Employee):
    def get_salary(self):
        return 15000
class Programmer(Employee):
    def __init__(self,name,working_hour=0):
        super().__init__(name)
        self.working_hour = working_hour
    def get_salary(self):
        return 200*self.working_hour
class Saleman(Employee):
    def __init__(self,name,sales=0):
        super().__init__(name)
        self.sales = sales
    def get_salary(self):
        return 1800 + self.sales*0.05
emps = [Manager('one'),Programmer('two'),Programmer('three'),Manager('four'),Saleman('six')]
for emp in emps:
    if isinstance(emp,Programmer):
        emp.working_hour = int(input(f'请你输入{emp.name}的工作时间:'))
    elif isinstance(emp,Saleman):
        emp.sales = float(input(f'请你输入{emp.name}的销售额:'))
    print(f'{emp.name}的本月工资为：¥{emp.get_salary():.2f}')
