#读写文本文件
file = open('致橡树.txt','r',encoding = 'utf-8')
print(file.read())
file.close()

file = open('致橡树.txt','r',encoding = 'utf-8')
for line in file:
    print(line,end='')
file.close()

file = open('致橡树.txt','r',encoding='utf-8')
lines = file.readlines()
for line in lines:
    print(line,end='')
file.close()
    #a,写入新内容
file = open('致橡树.txt','a',encoding = 'utf-8')
file.write('\n标题：《致橡树》')
file.write('\n作者：舒婷')
file.write('\n时间：1977年3月')
file.close()
#异常处理机制
file = None
try:
    file = open('致橡树.txt','r',encoding = 'utf-8')
    print(file.read())
except FileNotFoundError:
    print('无法打开指定文件')
except LookupError:
    print('指定了未知的编码！')
except UnicodeDecodeError:
    print('读取文件时解码错误')
finally:
    if file:
        file.close()
    #raise关键词来引发异常，抛出异常对象
class InputError(ValueError):
    pass
def fac(num):
    if num < 0:
        raise InputError('只能计算非负整数的阶乘')
    if num in (0,1):
        return 1
    return num * fac(num-1)

flag = True
while flag:
    num = int(input('n = '))
    try:
        print(f'{num}!={fac(num)}')
        flag = False
    except InputError as err:
        print(err)
#上下文管理器语法
try:
    with open('致橡树.txt','r',encoding = 'utf-8') as file:
        print(file.read())
except FileNotFoundError:
    print('无法打开指定文件')
except LookupError:
    print('制定了未知的编码')
except UnicodeDecodeError:
    print('读取文件时解码错误')
#读写二进制文件
try:
    with open('guido.jpg','rb') as file1:
        data = file1.read()
    with open('吉多.jpg','wb') as file2:
        file2.write(data)
except FileNotFoundError:
    print('指定文件无法打开')
except IOError:
    print('读写文件时出现错误')
print('程序执行结束')
