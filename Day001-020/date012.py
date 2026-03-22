#创建和使用字典
person = {
    'name' : '羽毛',
    'age' : 25,
    'height' : 170,
    'weight' : 60,
    'addr ' : '苏州市',
    'tel' : '123456',
    'emergence contact':'123456'
}
print(person)
person = dict(name = '王大锤', age = 55, height = 168, weight = 60, addr = '武汉市')
print(person)
print(len(person))      #5
for key in person:
    print(key)
item1 = dict(zip('abcdef','123456'))
print(item1)    #{'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6'}
item2 = dict(zip('ABCDE',range(1,10)))
print(item2)    #{'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
item3 = {x:x **3 for x in range(1,6)}
print(item3)    #{1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
#字典的运算（key必须是不可变类型）
person = {
    'name' : '王大锤',
    'age' : 35,
    'height' : 168,
    'weight' : 60,
    'addr' : ['成都市','北京市'],
    'car' : {
        'brand' : 'BMW X7',
        'maxSpeed' : '250',
        'length' : 5170,
        'width' : 2000,
        'height' : 1835,
        'displacement' : 3.0
    }
}
print(person)
print('name' in person)
print(person['name'])
person['age'] = 25
person['tel'] = '123456'
person['signature'] = 'pracitice makes perfect'
print(person)
    #循环遍历
for key in person:
    print(f'{key}:\t{person[key]}')
#字典的方法
person = {'name':'王大锤', 'age':25, 'height':178, 'addr':'成都市'}
print(person.get('name'))
print(person.get('sex'))
print(person.get('sex', '没有'))
print(person.keys())
print(person.values())
print(person.items())
for key,value in person.items():
    print(f'{key}:\t{value}')
person1 = {'name': '王大锤', 'age': 55, 'height': 178}
person2 = {'age': 25, 'addr':'成都市'}
person1.update(person2)
print(person1)      #{'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市'}
person1.pop('age')
print(person1)      #{'name': '王大锤', 'height': 178, 'addr': '成都市'}
print(person1.popitem())    #('addr', '成都市')
print(person1)      #{'name': '王大锤', 'height': 178}
person1.clear()
print(person1)      #{}
person = {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市'}
del person['age']
print(person)       #{'name': '王大锤', 'height': 178, 'addr': '成都市'}
#字典的应用
#eg1一段话中字母的出现次数
sentence = input('请你输入一段话：')
counter = {}
for ch in sentence:
    if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
        counter[ch] = counter.get(ch , 0) + 1
sorted_keys = sorted(counter, key = counter.get, reverse = True)
for key in sorted_keys:
    print(f'{key}出现了{counter[key]}次')
#eg2：在一个字典中保存了股票的代码和价格，找出股价大于100元的股票并创建一个新的字典。
stocks1 = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM' : 149.24,
    'ORCL': 48.44,
    'ACN' : 166.89,
    'FB'  : 208.09,
    'SYMC': 21.29
}
stocks2 = {key : value for key , value in stocks1.items() if value > 100}
print(stocks2)
