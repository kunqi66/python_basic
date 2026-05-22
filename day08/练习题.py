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
        self.__name == name
        self.__age == age
    def eat(self):
        print(f'{self.__name}在吃')
    def sleep(self):
        print(f'{self.__name}在睡')

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def bark(self):
        print(f'{self.__name}:狗叫')

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def meow(self):
        print(f'{self.__nane}:猫叫')

class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def fly(self):
        print(f'{self.__name}:鸟飞')
    def eat(self):
        print(f'{self.__name}鸟吃虫子')
        