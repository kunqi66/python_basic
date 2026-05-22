print('第12题')
product_price = {
    "苹果": 5.99,
    "香蕉": 3.50,
    "牛奶": 12.80,
    "面包": 8.50,
    "笔记本电脑": 4999.99,
    "无线耳机": 299.99,
    "运动鞋": 399.00,
    "保温杯": 69.90
}
ans1 = filter(lambda x:x[1]>100,product_price.items())
print(dict(ans1))
ans2 = sorted(product_price.items(),key=lambda x: x[1])
print(dict(ans2))

print('='*100)
print('第13题')
goods_stock = [
    {"商品名称": "苹果", "库存量": 120, "价格": 5.99},
    {"商品名称": "香蕉", "库存量": 85, "价格": 3.50},
    {"商品名称": "牛奶", "库存量": 200, "价格": 12.80},
    {"商品名称": "面包", "库存量": 150, "价格": 8.50},
    {"商品名称": "笔记本电脑", "库存量": 30, "价格": 4999.99},
    {"商品名称": "无线耳机", "库存量": 55, "价格": 299.99},
    {"商品名称": "运动鞋", "库存量": 78, "价格": 399.00},
    {"商品名称": "保温杯", "库存量": 99, "价格": 69.90}
]
ans1 = sorted(goods_stock,key=lambda x:x['库存量'])
print(ans1)
import heapq
ans2 = heapq.nlargest(3,goods_stock,key=lambda x:x['库存量'])
ans = [item['商品名称'] for item in ans2]
print(ans)
prs = [item['库存量'] for item in ans2]
print(sum(prs))

print('='*100)
print('第14题')

import random,math
def is_preim(x):
    if x<=1:
        return False
    flag = True
    for i in range(2,int(math.sqrt(x))):
        if x%i == 0:
            flag = False
            break
    return flag
lst =[random.randint(1,100) for i in range(10)]
ans = filter(is_preim,lst)
ans_sum=sum(list(ans))
print(ans_sum)
