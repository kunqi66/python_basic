print('=' * 100)
print('第一题')
class BankAccount:
    def __init__(self,account_number ,balance ,password):
        self.__account_number = account_number
        self.__balance = balance
        self.__password = password
    def deposit(self ,amount ,password):
        if self.__password == password:
            self.__balance += amount
        else:
            print('密码错误')
    def withdraw(self ,amount ,password):
        if self.__password == password:
            if amount <= self.__balance:
                self.__balance -=amount
            else:
                print('余额不足')
        else:
            print('密码错误')
    def check_balance(self,password):
        if self.__password ==password:
            return self.__balance
        else:
            return '密码错误'
    
    def set_password(self, old_password, new_password):
        if self.__password == old_password:
            self.__password = new_password
        else:
            print('旧密码输入错误')
    @property
    def account_number(self):
        return self.__account_number
    @account_number.setter
    def account_number(self,account_number):
        self.__account_number = account_number
    @property
    def balance(self):
        return self.__balance

b1=BankAccount('2839078819',765768875867,'123456')
print(b1.balance)
b1.account_number = '89789789798'

print('=' * 100)
print('第二题')
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print(f'{self.name}在吃')
    def sleep(self):
        print(f'{self.name}在睡')

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def bark(self):
        print(f'{self.name}:狗叫')

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def meow(self):
        print(f'{self.name}:猫叫')

class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def fly(self):
        print(f'{self.name}:鸟飞')
    def eat(self):
        print(f'{self.name}鸟吃虫子')
d1 =Dog('kk', 6)
d1.bark()
b1 = Bird('kk',2)
b1.eat()
b1.sleep()
b1.fly()
print(Bird.mro())


print('='*100)
print('第三题')
import math
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
    def perimeter(self):
        print(f'周长为：{(self.width + self.height) * 2}')
    def area(self):
        print(f'面积为：{self.height * self.width}')

class Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.radius = radius
    def perimeter(self):
        print(f'周长为{self.radius * 2 * math.pi}')
    def area(self):
        print(f'面积为{self.radius ** 2 * math.pi}')
class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        print(f'周长为：{self.a + self.b + self.c}')
    def area(self):
        p = (self.a + self.b + self.c)/2
        print(f'面积为：{math.sqrt(p * (p - self.a) * (p - self.b) * (p- self.c))}')
    
    
def print_shape_info(shape):
    shape.area()
    shape.perimeter()

rec1 = Rectangle(3,4)
cir1 = Circle(5)
tri1 = Triangle(3,4,5)
print_shape_info(rec1)
print_shape_info(cir1)
print_shape_info(tri1)

print('=' * 100)
print('第四题员工管理系统')
import abc
class Employee(abc.ABC):
    def __init__(self, name, id, base_salary):
        super().__init__()
        self.__name = name
        self.__id = id
        self.__base_salary = base_salary
    def get_details(self):
        pass
    @abc.abstractmethod
    def caculate_salary(self):
        return self.__base_salary
    @property
    def id(self):
        return self.__id
    def __repr__(self):
        return f'员工名称:{self.__name}   员工工号:{self.__id}'
class Manager(Employee):
    def __init__(self, name, id, base_salary, bonus):
        super().__init__(name, id, base_salary)
        self.__bonus = bonus
    def caculate_salary(self):
        return self.__bonus + super().caculate_salary()
class Developer(Employee):
    def __init__(self, name, id, base_salary, project_count):
        super().__init__(name, id, base_salary)
        self.__project_count = project_count
    def caculate_salary(self):
        return super().caculate_salary() * self.__project_count
class Intern(Employee):
    def __init__(self, name, id, base_salary, mentor):
        super().__init__(name, id, base_salary)
        self.__mentor = mentor
    def caculate_salary(self):
        return super().caculate_salary()
class Company:
    def __init__(self,emplpyee_list = []):
        self.__emplpyee_list = emplpyee_list
    def add_emplotee(self, emp):
        self.__emplpyee_list.append(emp)
    def remove_employee(self, emp_id):
        for index in range(len(self.__emplpyee_list)):
            if self.__emplpyee_list[index].id == emp_id:
                del self.__emplpyee_list[index]
                return
        print('该员工不存在')
    def get_total_salary(self, emp_id):
        for index in range(len(self.__emplpyee_list)):
            if self.__emplpyee_list[index].id == emp_id:
                return self.__emplpyee_list[index].caculate_salary()
        print('该员工不存在')
        return 0
    def list_all_employees(self):
        print([item for item in self.__emplpyee_list])
        
m34 = Manager('kk', '001', 8000, 7000)
de34 = Developer('kk', '002', 8000, 7)
in34 = Intern('kk', '003', 8000, 'dd')
comp1 = Company()
comp1.add_emplotee(m34)
comp1.add_emplotee(de34)
comp1.add_emplotee(in34)
print(comp1.get_total_salary('001'))
print(comp1.get_total_salary('002'))
print(comp1.get_total_salary('003'))
comp1.list_all_employees()
comp1.remove_employee('002')
comp1.list_all_employees()

print('=' * 100)
print('第五题图书馆借阅系统')
class LibraryItem:
    def __init__(self, item_id, title, is_borrowed):
        self.__item_id = item_id
        self.__title = title
        self.__is_borrowed =is_borrowed
    def __repr__(self):
        return f'id:{self.__item_id},书名:{self.__title},是否借出:{self.__is_borrowed}'
    @property
    def item_id(self):
        return self.__item_id
    @property
    def title(self):
        return self.__title
    def borrow(self):
        self.__is_borrowed = True
    def return_item(self):
        self.__is_borrowed = False
    def get_info(self):
        return f'编号:{self.__item_id},名称:{self.__title},是否可借:{'可' if self.__is_borrowed else '不可'}'
class Book(LibraryItem):
    def __init__(self, item_id, title, is_borrowed, author, pages):
        super().__init__(item_id, title, is_borrowed)
        self.__author = author
        self.__pages = pages
    def get_info(self):
        return super().get_info() + f'作者是：{self.__author} 有{self.__pages}页'
    def display_item_info(self):
        print(f'信息有：\n{self.get_info()}')
class DVD(LibraryItem):
    def __init__(self, item_id, title, is_borrowed, director, duration):
        super().__init__(item_id, title, is_borrowed)
        self.__director = director
        self.__duration = duration
    def get_info(self):
        return super().get_info() + f'目录：{self.__director} 有效期：{self.__duration}'
    def display_item_info(self):
        print(f'信息有：\n{self.get_info()}')
class Magazine(LibraryItem):
    def __init__(self, item_id, title, is_borrowed, issue_number):
        super().__init__(item_id, title, is_borrowed)
        self.__issue_number = issue_number
    def get_info(self):
        return super().get_info() + f'编号:{self.__issue_number}'
    def display_item_info(self):
        print(f'信息有：\n{self.get_info()}')
class Library:
    def __init__(self, itemlist = []):
        self.__itemlist = itemlist
    def add_item(self, item):
        self.__itemlist.append(item)
    def remove_item(self, item_id):
        for index in range(len(self.__itemlist)):
            if self.__itemlist[index].item_id == item_id:
                del self.__itemlist[index]
                return
    def search_by_title(self, title):
        for index in range(len(self.__itemlist)):
            if self.__itemlist[index].title == title:
                return self.__itemlist[index]
    def display_available_info(self):
        for item in self.__itemlist:
            print(item)
        print()
book1 =Book('001','钢铁是怎样练成的',False,'niu',2000)
dvd1 =DVD('002','钢铁',False,'dir','dur')
maga1 =Magazine('003','钢铁是怎样',False,900)
Lib = Library()
Lib.add_item(book1)
Lib.add_item(dvd1)
Lib.add_item(maga1)
Lib.display_available_info()
Lib.remove_item('001')
Lib.display_available_info()
print(Lib.search_by_title('钢铁'))
# 演示多态
def display_item_info(item):
    item.display_item_info()
display_item_info(dvd1)
display_item_info(maga1)
display_item_info(book1)