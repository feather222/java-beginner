#字符串
    #转义字符\
s1 = '\'hello,world!\''
s2 = '\\hello,world!\\'
print(s1)   #'hello,world!'
print(s2)   #\hello,world!\
    #原始字符串
s1 = '\it \is \time \to \read \now'
s2 = r'\it \is \time \to \read \now'
print(s1)
"""ead 
ow"""
print(s2)   #\it \is \time \to \read \now
    #字符的特殊表示
s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1)   #abcabc
print(s2)   #骆昊
#字符串的运算
    #拼接和重复
s1 = 'hello' + '，' + 'world'
print(s1)   #hello，world
s2 = '!'* 3
print(s2)   #!!!
s1 +=s2
print(s1)   #hello，world!!!
s1 *= 2
print(s1)   #hello，world!!!hello，world!!!
    #字符串比较运算：实质上是编码数的大小比较
s1 = '羽毛'
s2 = 'hello world'
print(ord('羽'))     #32701
print(ord('毛'))     #27611
print(s1 > s2)      #True
    #成员运算
s1 = 'hello, world'
s2 = 'goodbye, world'
print('wo' in s1)   #True
print(s2 in s1)     #False
    #获取字符串长度
s = 'goodbye world'
print(len(s))       #13
    #索引和切片
s = 'qaz123'
n = len(s)
print(s[0],s[-n])   #q q
print(s[::-1])      #321zaq
#字符的遍历
s = 'hello'
for i in range(len(s)):
    print(s[i],end='\t')    #h	e	l	l	o
for elem in s:
    print(elem,end='\t')    #h	e	l	l	o
s1 = 'hello，world！'
s2 = 'GOODBYE,WORLD'
    #字符串首字母大写
print(s1.capitalize())  #Hello，world！
    #字符串每个首字母大写
print(s1.title())       #Hello，World！
    #大小写转换
print(s1.upper())       #HELLO，WORLD！
print(s2.lower())       #goodbye,world
    #正反向查找操作
s = 'hello,world'
print(s.find('o'))
print(s.rfind('o'))
print(s.find('o',9))
print(s.index('o'))
print(s.rindex('o'))
print(s.index('o',9))
"""
4
7
-1
4
7
ValueError
"""
    #性质判断
s1 = 'qaz123'
print(s1.startswith('Qa'))  #False
print(s1.endswith('12'))    #False
print(s1.endswith('12'))    #False
print(s1.isdigit())         #False
print(s1.isalpha())         #False
print(s1.isalnum())         #True
    #格式化
a = 321
b = 123
print('%d * %d = %d'%(a,b,a*b))             #321 * 123 = 39483
print('{0}*{1}={2}'.format(a,b,a*b))  #321*123=39483
print(f'{a}*{b}={a*b}')                     #321*123=39483
    #修剪操作
s1 = '~hello world~'
print(s1.strip('~'))    #hello world
print(s1.lstrip('~'))   #hello world~
print(s1.rstrip('~'))   #~hello world
    #替换操作,第三个位置为替换次数，而不是位置
s = 'hello,good world'
print(s.replace('o','!'))           #hell!,g!!d w!rld
print(s.replace('o','@',2))   #hell@,g@od world
    #拆分与合并
s1 = 'I love you so much'
words = s1.split()
print(words)        #['I', 'love', 'you', 'so', 'much']
s2 = '~'.join(words)
print(s2)           #I~love~you~so~much
words = s2.split('~')
print(words)        #['I', 'love', 'you', 'so', 'much']
words = s2.split('~',2)
print(words)        #['I', 'love', 'you~so~much']
#编码和解码
a = '羽毛'
b = a.encode('utf-8')
c = a.encode('gbk')
print(b)                    #b'\xe7\xbe\xbd\xe6\xaf\x9b'
print(c)                    #b'\xd3\xf0\xc3\xab'
print(b.decode('utf-8'))    #羽毛
print(c.decode('gbk'))      #羽毛
