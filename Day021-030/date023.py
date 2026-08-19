#python读写csv文件
#使用csv模块的writer函数
import csv
import random
with open('scores.csv','w') as file:
    writer = csv.writer(file,delimiter='|',quoting=csv.QUOTE_ALL)
    writer.writerow(['name','chinese','math','english'])
    names = ['关羽','张飞','赵云','马超','黄忠']
    for name in names:
        scores = [random.randrange(50,101) for _ in range(3)]
        scores.insert(0,name)
        writer.writerow(scores)
#从csv文件读取数据
import csv
with open('scores.csv','r') as file:
    reader = csv.reader(file,delimiter = '|')
    for data_list in reader:
        print(reader.line_num,end='\t')
        for elem in data_list:
            print(elem,end='\t')
        print()
