# 函数是一种数据类型
# 定义函数
def my_function():
    print("我是函数体")

# 打印函数的类型
print(type(my_function))


# 函数可以作为参数传递
def say_hi():
    print("Hi!")


def call_function(func):
    func()  # 这里要求传给func的实参是一个函数。


call_function(say_hi)  # say_hi是一个函数，它作为参数被传给了call_function函数


student_list = [{"name": "zhang3", "age": 36}, {"name": "li4", "age": 14}, {"name": "wang5", "age": 27}]
map_result = map(lambda s: s["name"], student_list)
print("姓名：", list(map_result))

"""
    匿名函数作为返回值
"""
def get_func(operate):

    match operate:
        case "add":
            return lambda a, b: a + b
        case "sub":
            return lambda a, b: a - b
        case "mul":
            return lambda a, b: a * b
        case "div":
            return lambda a, b: a / b
        case _:
            return None

func = get_func("add")(2,5)
print(func)
#print(f"{func.__name__}的结果：", func(1,2))