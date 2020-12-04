# \ 转译 \n换行 \t表示制表符，\\ r表示默认不转译
# i'm "ok"
print('i\'m,\"ok\"')
print('I\'m learning\nPython.')
print('\\\n\\')
# '''表示多行换行
print('''...line1
...line1
...line1''')
print(r'''hello,\n
world''')
# 布尔值
print(3 > 2)  # T F 开头大写 逻辑运算符 直接用英文
True and False
# if 判断语句
age = 18
if age > 18:
    print('tab1')
else:
    print('tab2')
    a = 'ABC'
    b = a
    a = 'XYZ'
    print(b)
# 除法运算 精确除法，底板除法
print(10/3)
print(9/3)
print(10//4)  # 向下取整
# 求余数
print(10 % 3)
# print 练习
n = 123
f = 456.789
s1 = 'hello,word'
s2 = 'hello,\'Adam\''
s3 = r'hello,"Bart"'
s4 = r'''Hello,
Lisa!'''
print(n,f,s1,s2,s3,s4)