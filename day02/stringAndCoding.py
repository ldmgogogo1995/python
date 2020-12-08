# utf-8编码 ，python的字符串是Unicode编码，也就是说python支持多语言
print('包含中文的str')
# 对于单个的字符编码 Python 提供了ord() 获取字符串的整数表示，chr()把编码转换成对应的字符:
print(ord('A'))
print(ord('间'))
print(chr(66))
print(chr(25991))
# 如果知道字符的整数编码，还可以用十六进制这么写str:
print('\u4e2d\u6587')
# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
# Python对bytes类型的数据用带b前缀的单引号或双引号表示:
x = b'ABC'
print(x)
# Unicode表示的str通过encode(方法)
print('zhongwen'.encode('ascii'))
# print('中文'.encode('ascii'))报错
print('中文'.encode('utf-8'))
# 既然有转码，那一定有解码(decode)
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))  # 忽略错误字节
# len()方法，求出字符串包含多少个字符
print(len('nimasile'))
# len方法同样可以求字节数
print(len('中文'.encode('utf-8')))
# 占位符 %
print('Hello, %s' % 'world')
print('hi,%s,you have $%d' % ('Michael', 100000000000))
# 常用占位符：
# %d 整数
# %f 浮点数
# %s 字符串
# %x 十六进制整数
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
# 如果你不确定改用什么%s永远起作用
print('Age:%s. Gender: %s' % (25, True))
#另一种方法是format方法
print('Hello , {0},成绩提升了 {1:.1f}%'.format('小明',17.125))
#f-string