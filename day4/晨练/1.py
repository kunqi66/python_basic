num_sum = 0
co = 100
while co <= 1000:
    num_sum += co
    co += 1
print(num_sum)

for i in range(100,1000):
    a = i%10
    b = i//10%10
    c = i//100
    if a**3+b**3+c**3==i:
        print(i,end=" ")
print()

s_str = 'hello world'
for i in range(-1,-len(s_str)-1,-1):
    print(s_str[i],end="")


list_demo =[20,90,5,4,6,1,2,90,9,90,55,90,56,90]
while 90 in list_demo:
    list_demo.remove(90)
print(list_demo)