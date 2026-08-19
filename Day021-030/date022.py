#读写JSON格式的数据
import json
my_dict = {
    'name':'yumao',
    'age':25,
    'friends':['狄仁杰','李元芳'],
    'cars':[
        {'brand':'BMW','max_speed':240},
        {'brand':'Audi','max_speed':280},
        {'brand':'Benz','max_speed':280}
    ]
}
print(json.dumps(my_dict))
#{"name": "yumao", "age": 25, "friends": ["\u72c4\u4ec1\u6770", "\u674e\u5143\u82b3"], "cars": [{"brand": "BMW", "max_speed": 240}, {"brand": "Audi", "max_speed": 280}, {"brand": "Benz", "max_speed": 280}]}
#转换后，再写入
with open('data.json','w') as file:
    json.dump(my_dict,file)
import json
with open('data.json','r') as file:
    my_dict = json.load(file)
    print(type(my_dict))
    print(my_dict)
#使用网络API获取数据
import requests
resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
if resp.status_code == 200:
    data_model = resp.json()
    for news in data_model['newslist']:
        print(news['title'])
        print(news['url'])
        print('_'*60)   #打印 60 个减号（-），形成一条分隔线，用于区分不同新闻的输出内容
