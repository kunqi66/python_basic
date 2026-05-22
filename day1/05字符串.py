# 序列类型之字符串类型
a = 'hello'  # 字符串可以是单引号
print("a = 'hello'的类型：", type(a))

a = "hello"  # 字符串可以是双引号
print('a = "hello"的类型', type(a))

# 多行文本可以使用"""
a = """
    hello
    world
"""
# 多行文本也可以使用'''
a = '''
    hello
    atguigu
'''
print("a的类型",type(a))

# 转义字符
a = "hello\tworld\njava"
print(a)

# 在多行文本中行尾的\表示不换行，或者续行符
a = """
    hello\
    world
"""
print(a)

# 字符串intern机制：创建字符串对象时，如果字符串对象已经创建过，那么Python解释器就会返回之前创建的字符串对象，从而节省内存开销
a = "hello"
b = "hello"
print(a is b)