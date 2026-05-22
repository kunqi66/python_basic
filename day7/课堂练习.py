import types

print('第一题学生信息管理系统')
class Student:
    school_name = '第一中学'
    student_count = 0

    def __init__(self, name, age, class_name):
        self.name = name
        self.age =age
        self.class_name = class_name
        Student.student_count_sum()
    def introduce(self):
        print(f'姓名：{self.name},年龄：{self.age},班级：{self.class_name}')
    def have_birthday(self):
        self.age+=1
        print(f'{self.name}同学生日快乐')
    @classmethod
    def student_count_sum(cls):
        cls.student_count += 1
    @classmethod
    def change_school(cls,name):
        cls.school_name = name
    @classmethod
    def get_student_count(cls):
        return cls.student_count
    @staticmethod
    def is_valid_age(age):
        return 6<= age <= 18

s1 = Student('张三',13,'yiban')
s2 = Student('lisi',14,'erban')
s3 = Student('wangwu',13,'yiban')
s1.introduce()
s2.introduce()
s3.introduce()
s3.have_birthday()
Student.change_school('第二中学')
print(Student.school_name)
print(Student.get_student_count())
print(Student.is_valid_age(14))
print(Student.is_valid_age(19))
print(Student.is_valid_age(2))

print('='*100)
print('第二题简单的购物车管理系统')
class Goods:
    def __init__(self, title, price):
        self.title = title
        self.price = price
    def __repr__(self):
        return f'（商品为{self.title}  价格为：{self.price})'
class ShoppingCart:
    store_name ='kk小店'
    total_carts = 0
    def __init__(self, owner, items:list, total_price):
        self.owner = owner
        self.items = items
        self.total_price = total_price
        ShoppingCart.add_total_carts()

    def add_item(self, item_name, price):
        item = Goods(item_name,price)
        self.items.append(item)
        self.total_price += price
    def remove_item(self,item_name):
        for index in range(len(self.items)):
            if self.items[index].title == item_name:
                self.total_price-=self.items[index].price
                del self.items[index]
                ShoppingCart.total_carts -= 1
    def show_carts(self):
        print('{}的购物车'.format(self.owner))
        print(self.items)
        print(self.total_price)

    @classmethod
    def add_total_carts(cls):
        cls.total_carts += 1
    @classmethod
    def set_store_name(cls,new_name):
        cls.store_name = new_name
    @classmethod
    def show_total_carts(cls):
        print(cls.total_carts)
    @staticmethod
    def calculate_discount(price, discount_rate):
        return price*discount_rate

car1 = ShoppingCart('qikun',[],0)
car2 = ShoppingCart('wqin',[],0)
car1.add_item('笔',8.9)
car1.add_item('纸',10.9)
car1.add_item('包',20.5)
car1.show_carts()
car1.remove_item('包')
car1.show_carts()
ShoppingCart.set_store_name('qq的小店')
print(ShoppingCart.store_name)
print(ShoppingCart.calculate_discount(89, 0.8))


print('='*100)
print('第三题图书管理系统')
class Book:
    library_name = ''
    total_books = 0
    def __init__(self, title, auther ,is_borrowed = False):
        self.title = title
        self.auther = auther
        self.is_borrowed = is_borrowed
        Book.total_books += 1
    def borrow(self):
        if self.is_borrowed:
            print('图书已经被借出')
        else:
            self.is_borrowed = True
    def return_book(self):
        self.is_borrowed = False
    def display_info(self):
        print(f'图书名称为{self.title}，图书作者为{self.auther}')
    @classmethod
    def change_library_name(cls, new_name):
        cls.total_books = new_name
    @classmethod
    def get_total_books(cls):
        return cls.total_books
    @staticmethod
    def is_valid_book(book_title):
        if book_title:
            if len(book_title)>0:
                return True
            else:
                return False
        else:
            return False
book1 = Book("钢铁是怎样炼成的",'d')
book2 = Book("毛泽东选集",'m')
book3 = Book("明朝那些事儿",'当年明月')
book1.borrow()
book1.borrow()
book1.return_book()
book1.display_info()
book2.display_info()
book3.display_info()
Book.change_library_name('人民的图书馆')
print(Book.is_valid_book('dsa'))
print(Book.is_valid_book(None))
print(Book.is_valid_book(''))

print('='*100)
print('第四题动态修改类和实例')
class Car:
    wheels = 4
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
    def drive(self):
        print('汽车正在行驶')
car1 = Car('比亚迪','black')
car1.engine = "v6,3.0T"
car1.color = "green"
del car1.color
Car.fuel_type = '#98'
Car.wheels =6
@classmethod
def show_info(cls):
    print('动态添加类方法')
Car.d_show_info = show_info
Car.d_show_info()
def stop(self):
    print(f'{self.brand}停止了')
car1.d_stop = types.MethodType(stop,car1)
car1.d_stop()
del car1.d_stop
# car1.d_stop()

print('='*100)
print('第五题综合案例银行账户系统')
class BankAccount:
    bank_name = ''
    total_accounts = 0
    interest_rate = 0.03
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        BankAccount.total_accounts += 1
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('余额不足')
    def check_balance(self):
        return self.balance
    def apply_interest(self):
        self.balance += self.balance * BankAccount.interest_rate
    @classmethod
    def change_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts
    @classmethod
    def create_account(cls,owner):
        number = 'BANK'+'10001'+str(cls.total_accounts+1)
        account = BankAccount(number,owner,0)
        return account
    @staticmethod
    def validate_amount(amount):
        if amount > 0:
            return True
        else:
            return False
    @staticmethod
    def format_currency(amount):
        return '￥'+str(amount)
acc1 = BankAccount.create_account('kk')
acc2 = BankAccount.create_account('dzmn')
acc3 = BankAccount.create_account('fd')
print(acc1.check_balance())
acc1.deposit(10000.0)
print(acc1.check_balance())
acc1.withdraw(3490.3)
print(acc1.check_balance())
acc1.apply_interest()
print(acc1.check_balance())
BankAccount.change_interest_rate(0.09)
acc1.apply_interest()
print(acc1.check_balance())
print(BankAccount.validate_amount(4565))
print(BankAccount.validate_amount(0))
print(BankAccount.validate_amount(-90978))
print(BankAccount.format_currency(3242134))