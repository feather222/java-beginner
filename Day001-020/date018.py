#可见性和属性装饰器
class Student:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def study(self,course_name):
        print(f'{self.__name}正在学习{course_name}')
stu = Student('羽毛','20')
stu.study('Python程序设计')      #羽毛正在学习Python程序设计
print(stu._Student__age)       #羽毛
#动态属性
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
stu = Student('羽毛',23)
stu.sex = 'male'
print(stu.sex)
    #禁止动态添加属性__slots__
class Student:
    __slots__ = ('name','age')
    def __init__(self,name,age):
        self.name = name
        self.age = age
stu = Student('羽毛',23)
stu.sex = '男'       #AttributeError: 'Student' object has no attribute 'sex'
#静态方法和类方法
class Triangle(object):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    @staticmethod
    def is_valid(a,b,c):
        return a + b > c and a + c > b and b + c > a
    def perimeter(self):
        return self.a + self.b + self.c
    def area(self):
        l = self.perimeter()/2
        return (l*(l-self.a)*(l-self.b)*(l-self.c))**0.5
if Triangle.is_valid(3,4,5):
    t = Triangle(3,4,5,)
    print(f'周长为{t.perimeter()}')
    print(f'面积为{t.area()}')
else:
    print('无效的边长!!!')
    #装饰器转换为属性
class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    @classmethod
    def is_valid(cls,a,b,c):
        return a + b > c and a + c > b and b + c > a
    @property
    def perimeter(self):
        return self.a + self.b + self.c
    @property
    def area(self):
        l = self.perimeter / 2
        return (l*(l-self.a)*(l-self.b)*(l-self.c))**0.5
if Triangle.is_valid(2,3,4):
    t = Triangle(2,3,4)
    print(f'周长为:{t.perimeter:.2f}')
    print(f'面积为:{t.area:.2f}')
else:
    print('无效边长！！！')
#继承和多态,父类和子类
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print(f'{self.name}正在吃饭')
    def sleep(self):
        print(f'{self.name}正在睡觉')
class Student(Person):
    def __init__(self,name,age):
        super().__init__(name,age)
    def study(self,course_name):
        print(f'{self.name}正在学习{course_name}')
class Teacher(Person):
    def __init__(self,name,age,title):
        super().__init__(name,age)
        self.title = title
    def teach(self,course_name):
        print(f'{self.name}{self.title}正在讲授{course_name}.')
stu1 = Student('first',21)
stu2 = Student('second',22)
tea1 = Teacher('third',33,'doctor')
stu1.eat()
stu2.sleep()
tea1.eat()
tea1.teach('Python程序设计')
