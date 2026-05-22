import random as rd
# print('1题')
# li = [rd.randint(1,100) for i in range(10)]
# print(li)
# print(len(li), '最大' ,max(li), '最小' ,min(li))
# print('总和',sum(li))
# print(li[5])
# print(li[-3:])
# print(li.count(50))
# for (i,j) in enumerate(li):
#     print(i,j,end='    ')
# print()
# print('='*100)
#
# print('2题')
# scores = [78, 92, 85, 69, 100, 88, 75, 92, 100, 85]
# print('平均分:{:.1f}'.format(sum(scores)/len(scores)))
# print('最高分:',max(scores),'最低分:',min(scores))
# if scores.count(100):
#     print(f'有{scores.count(100)}个100分')
# else:
#     print('没有100分')
# pre_li = scores[:5]
# print(pre_li)
# print(f'5个平均分:{sum(pre_li)/5:.1f}')
# for (index,score) in enumerate(scores):
#     print(f'第{index+1}个学生成绩是{score}',end='  ')
# print()
#
#
# print('='*100)
# print('3题')
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numbers = [i for i in numbers if i%2!=0]
# print( numbers)
#
# print('='*100)
# print('4题')
# fruits = []
# fruits.append('apple')
# fruits.append('banana')
# fruits.append('cherry')
# fruits.append('data')
# fruits.insert(0,'elderberry')
# fruits.insert(3,'fig')
# fruits[-1] = 'grape'
# print( fruits)
#
# print('='*100)
# print('5题')
# prices = [10.5, 20.0, 15.75, 8.2, 12.0]
# new_prices = [price * 1.1 for price in prices]
# print(new_prices)
#
#
# print('='*100)
# print('6题')
# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9, 10]
# combined_list = list1 + list2
# combined_list.sort(reverse=True)
# print(combined_list)
#
# print('='*100)
# print('7题')
# l1 = list(input('请输入一个字符串: '))
# l2 = [ele for ele in l1 if (ord(ele) in range(ord('a'),ord('z')+1)) or (ord(ele) in range(ord('A'),ord('Z')+1))]
# print(l2)
#
# print('='*100)
# print('8题')
# maxl_str = ''
# while True:
#     str1 = input('请输入一个字符串: ')
#     if str1 == 'exit':
#          break
#     if len(str1) > len(maxl_str):
#         maxl_str = str1
# print(maxl_str)

# print('='*100)
# print('9题')
# ans =set()
# while len(ans) < 10:
#     num = rd.randint(1,100)
#     if num%2 == 0:
#         ans.add(num)
# print( ans )
#
# print('='*100)
# print('10题')
# set_1 = {1, 2, 3, 4, 5}
# set_2 = {3, 4, 5, 6, 7}
# set_1.update(set_2)
# print(set_1)

print('='*100)
print('11题')
str1 = "Atguigu is a Good place"
str1=str1.upper()
ans = {}
for s in str1:
    if s ==' ':
        continue
    if not (s in ans):
        ans[s]=str1.count(s)
    else:
        continue
max_num=0
j=[]
for (k,v) in ans.items():
    if v>max_num:
        max_num = v
        j = [k]
    elif v == max_num:
        j.append(k)
print(j)

print('='*100)
print('12题')
student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 88}
student_scores['Lily'] = 60
print(student_scores['Alice'])
del student_scores['Bob']
updated_scores = {k: v+5 for (k,v) in student_scores.items()}
print(updated_scores)

print('='*100)
print('13题')
fruit_prices = {"apple": 1.2, "banana": 0.5, "cherry": 2.5, "date": 3.0}
max_key = ''
max_price = 0.0
for (fruit,price) in fruit_prices.items():
    if price > max_price:
        max_price = price
        max_key = fruit
print(max_key,'的价格',max_price)