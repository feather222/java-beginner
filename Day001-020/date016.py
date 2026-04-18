#装饰器
import random
import time
def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.random()*6)
    print(f'{filename}下载完成.')
def upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.random()*8)
    print(f'{filename}上传完成。')
download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')
    #计算上传下载时间
start = time.time()
download('MySQL从删库到跑路.avi')
end = time.time()
print(f'花费时间{end-start:.3f}秒')
    #recor_time装饰器
import time
import random
def record_time(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f'{func.__name__}执行时间为：{end-start:.2f}秒')
        return result
    return wrapper
def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.random()*6)
    print(f'{filename}下载完成.')
def upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.random()*8)
    print(f'{filename}上传完成。')

download = record_time(download)
upload = record_time(upload)
download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')
    #record_time语法糖
import random
import time
def record_time(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f'{func.__name__}执行时间为：{end-start:.2f}秒')
        return result
    return wrapper
@record_time
def dowload(filename):
    print(f'{filename}开始下载')
    time.sleep(random.random()*6)
    print(f'{filename}下载完成')
@record_time
def upload(filename):
    print(f'{filename}开始上传')
    time.sleep(random.random()*8)
    print(f'{filename}上传完成')
dowload('MySQL从删库到跑路')
upload('Python从入门到入土')
    #__wrapped__属性
import random
import time
from functools import wraps
def record_time(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f'{func.__name__}执行时间为{end-start:.2f}秒')
        return result
    return wrapper
@record_time
def download(filename):
    print(f'{filename}开始下载')
    time.sleep(random.random()*6)
    print(f'{filename}下载结束')
@record_time
def upload(filename):
    print(f'{filename}开始上传')
    time.sleep(random.random()*8)
    print(f'{filename}上传结束')
download('MySQL从删库到跑路')
upload('Python从入门到入土')
download.__wrapped__('MySQL必知必会.pdf')
upload.__wrapped__('Python从新手到大师.pdf')
#递归调用
def fac(num):
    if num in (0,1):
        return 1
    return num*fac(num-1)
print(fac(5))
#斐波那契数列
def fib1(n):
    if n in (1,2):
        return 1
    return fib1(n-1)+fib1(n-2)
for i in range(1,51):
    print(fib1(i))
    #直接法
def fib2(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b,a+b
    return a
    #lru_cache
from functools import lru_cache
@lru_cache()
def fib1(n):
    if n in (1,2):
        return 1
    return fib1(n-1)+fib1(n-2)
for i in range(1,51):
    print(i,fib1(i))
