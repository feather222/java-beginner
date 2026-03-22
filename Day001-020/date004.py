#分支结构
#if和else构建分支结构

weight = float(input('请输入你的体重值kg'))
height = float(input('请输入你的身高值m'))
BMI=weight/height**2
print(f'{BMI=:.1f}')
if 18.5 <= BMI <24:
    print('体重正常')
elif BMI < 18.5:
    print('体重过轻')
else:
    print('体重过重')
#使用match和case构造分支结构
status_code = int(input('相应状态码；'))
match status_code:
    case 400 | 405:
        description = 'Invalid Request'
    case 401 | 403 | 404:
        description = 'Not Found'
    case 418:
        description = 'I am a teapot'
    case 429: 
        description = 'Too Many Requests'
    case _:
        description = 'Unknown Error'
print('状态码描述',description)
#分支结构的应用
#eg1分段函数计算
x = float (input('请输入x的数值'))
if x > 1:
    y = 3*x-5
elif x < -1:
    y = 5*x+3
else:
    y = x+2
print(f'{y=:.1f}')
#百分之成绩登记转换
score = float(input('请输入你的成绩'))
if score >= 90:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score <= 80:
    grade = 'C'
else:
    grade = 'D'
print(f'{grade = }')#不如print(f'您的成绩登记是 {grade} ')
#计算三角形周长与面积
a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
if a + b > c and a + c > b and b + c > a:
    perimeter = a + b + c
    print(f'周长{perimeter = }')
    s = perimeter / 2
    area = (s * (s - a)*(s - b)*(s - c))**0.5
    print(f'{area =: .1f}')
else:
    print('Error')
