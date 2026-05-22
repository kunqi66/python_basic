class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def eat(self):
        print(f"{self.name}吃东西....")

# 定义子类
class Student(Person):
    def __init__(self, name,age,score): # 子类构造方法
        super().__init__(name,age) # 调用父类的构造方法，为继承的name和age初始化代码
        self.score = score

    def study(self):
        print(f"{self._name}在学习，年龄为{self._age}，得分为{self.score}")
s1 =Student('kk',78,99)
s1.study()