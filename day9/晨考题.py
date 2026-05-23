print('='*100)
print('第一题')
class Vehicle:
    def __init__(self, base_rate, rent_days):
        self.__base_rate = base_rate
        self.__rent_days = rent_days
    def calculate_cost(self):
        return self.__base_rate * self.__rent_days
    def set_base_rate(self, new_rate):
        self.__rent_days =new_rate
    @property
    def rent_days(self):
        return self.__rent_days
class Car(Vehicle):
    def __init__(self, base_rate, rent_days):
        super().__init__(base_rate, rent_days)
    def calculate_cost(self):
        return super().calculate_cost() + self.rent_days *50
class Truck(Vehicle):
    def __init__(self, base_rate, rent_days):
        super().__init__(base_rate, rent_days)
    def calculate_cost(self, km):
        return super().calculate_cost() + km * 5
c1 =Car(5000,10)
print(c1.calculate_cost())
t1 =Truck(5000,10)
print(t1.calculate_cost(90))
c1.set_base_rate(45)
print(c1.rent_days)

print('='*100)
print('第二题')
class Fighter:
    def __init__(self, strength):
        self.__strength = strength
    def attack(self):
        print('输出物理攻击'+str(self.__strength))
    def get_power(self):
        return self.__strength
    @property
    def strength(self):
        return self.__strength
class Mage:
    def __init__(self, intelligence):
        self.__intelligence = intelligence
    def cast_spell(self):
        print('输出火球术'+str(self.__intelligence))
    def get_power(self):
        return self.__intelligence
    @property
    def intelligence(self):
        return self.__intelligence
class Healer:
    def __init__(self, wisdow):
        self.__wisdow = wisdow
    def heal(self):
        print('治疗术' + str(self.__wisdow))
    def get_power(self):
        return self.__wisdow
    @property
    def wisdow(self):
        return self.__wisdow
class Paladin(Fighter, Healer):
    def __init__(self, strength, wisdow):
        super().__init__(strength)
        Healer.__init__(self, wisdow)
    def holy_light(self):
        print('圣光普照')
    def get_power(self):
        return super().get_power() * 0.5 + Healer.get_power(self) * 0.4
class Spellblade(Fighter, Mage):
    def __init__(self, strength, intelligence):
        super().__init__(strength)
        Mage.__init__(self, intelligence)
    def attack(self):
        self.cast_spell()
        super().attack()
    def get_power(self):
        return super().get_power() * 0.5 +Mage.get_power(self) * 0.5
f1 = Fighter(500)
m1 = Mage(60)
h1 = Healer(70)
p1 = Paladin(500, 90)
s1 = Spellblade(600, 70)
def show_power(item):
    print(item.get_power())
show_power(f1)
show_power(m1)
show_power(h1)
show_power(p1)
show_power(s1)
f1.attack()
m1.cast_spell()
h1.heal()
p1.attack()
s1.attack()
    
        