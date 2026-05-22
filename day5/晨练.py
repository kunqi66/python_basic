print('第一题')
nums = [1,2,3,4,5]
nums.append(6)
nums.insert(0,0)
print(nums)

print('='*20)
lst =[10,20,30,20,40,20]
for (index,item) in enumerate(lst):
    if item == 20:
        del lst[index]
        break
print(lst)

print('='*20)
scores = [88,92,76,90,85]
num_sum = sum(scores)
num_avg = num_sum/len(scores)
print(f'{num_sum}  {num_avg}')

print('='*20)
lst = [1,2,3,4]
lst.sort(reverse=True)
print(lst)

print('='*20)
fruits = ['apple','banana','orange']
if 'apple' in fruits:
    print(True)
else:
    print(False)

print('='*100)
print('第二题')
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1 | s2)
print(s1 & s2)

print('='*20)
s = {1,2}
s.add(3)
s.discard(1)
print(s)

print('='*20)
a = {1, 2}
b = {1, 2, 3}
f = True
for item in a:
    if not(item in b):
        f =False
if f:
    print("a是b的子集")
else:
    print("a不是b的子集")

print('='*20)
lst1 = [1,2,3,4]
lst2 = [3,4,5,6]
s = set(lst1) & set(lst2)
print(list(s))

print('='*20)
lst = {5, 2, 5, 1, 2, 1, 3}
s = set(lst)
print(list(s).sort())

print('='*100)
print('第三题')
s='Hello Python 123'
num_count = 0
for item in s:
    if 'a' <= item <='z' or 'A'<= item <= 'Z':
        num_count += 1
print(num_count)

print('='*20)
name = "   python learner    "
name = name.strip().upper()
print(name)

print('='*20)
s = 'abcdefg'
print(s[2:6])

print('='*20)
tel1='13800128000'
f = True
for item in tel1:
    if not('0'<= item <='9'):
        f = False
if f:
    print('是纯数字')
else:
    print('不是纯数字')

print('='*20)
words = "python-java-c++"
ans = words.split('-')
print(ans)
