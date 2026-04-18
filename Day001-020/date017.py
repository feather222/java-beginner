#定义类别
class Student:
    def study(self,course_name):
        print(f'学生正在学习{course_name}.')
    def paly(self):
        print(f'学生正在玩游戏.')
#创建和使用对象
stu1 = Student()
stu2 = Student()
print(stu1)
print(stu2)
print(hex(id(stu1)),hex(id(stu2)))
"""
<__main__.Student object at 0x000001F7AFAAD050>
<__main__.Student object at 0x000001F7AFAAD390>
0x1f7afaad050 0x1f7afaad390
"""
#通过‘类.方法’调用方法，第一个参数是接收消息的对象，第二个参数是学习的课程名称
Student.study(stu1,'Python程序设计')    #学生正在学习Python程序设计.
#通过‘对象.方法’调用，“.”前边就是对象，只需要传入第二个参数
stu1.study('Python程序设计')                        #学生正在学习Python程序设计.
Student.paly(stu2)  #学生正在玩游戏.
stu2.paly()         #学生正在玩游戏.
#初始化方法
    #定义类别
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def study(self,course_name):
        print(f'{self.name}正在学习{course_name}')
    def paly(self):
        print(f'{self.name}正在玩游戏')
    #创建对象
stu1 = Student('羽毛',44)
stu2 = Student('林志颖',25)
Student.study(stu1,'Python程序设计')
stu1.study('Python程序设计')
#目标对象的发起者
import time
class Clock:
    def __init__(self,hour=0,min=0,sec=0):
        self.hour = hour
        self.min = min
        self.sec = sec
    def run(self):
        self.sec += 1
        if self.sec ==60:
            self.sec = 0
            self.min += 1
            if self.min ==60:
                self.min = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0
    def show(self):
        return f'{self.hour:0>2d}:{self.min:0>2d}:{self.sec:0>2d}'
clock = Clock(23,59,58)
while True:
    print(clock.show())
    time.sleep(1)
    clock.run()
#平面上的点
class Point:
    def __init__(self,x=0,y=0):
        self.x ,self.y = x,y
    def distance_to(self,other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx**2+dy**2)**0.5
    def __str__(self):
        return f'({self.x},{self.y})'
p1 = Point(3,5)
p2 = Point(6,9)
print(p1)
print(p2)
print(p1.distance_to(p2))
