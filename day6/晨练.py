import math
print('第一题')
keys = ["name",'age','gender']
values = ['小李','22','男']
ans = {}
for i in range(len(keys)):
    ans[keys[i]] = values[i]

print('='*100)
print('第二题')
def calculate(a,b):
    if b == 0:
        return None
    ans1 = a //b
    ans2 = a % b
    return ans1,ans2
print(calculate(15,4))

print('='*100)
print('第三题')
def greet(name,message = 'hello'):
    return message+' '+name
print(greet('Alice'))

print('='*100)
print('第四题')
def find_all_even(*lst):
    ans1 = [item for item in lst if item%2 == 0]
    return ans1
print(find_all_even(1,2,3,4,5,6,7,8,9))

print('='*100)
print('第五题')
def square(a):
    return a*a

def cube(a):
    return a * square(a)

def volume(r):
    return 4*(cube(r)*math.pi)/3

print(volume(5.6))