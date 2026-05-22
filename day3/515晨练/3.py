num_a = int(input("请输入男生人数:"))
num_b = int(input("请输入女生人数:"))
unm_sum = num_a+num_b
print(f'男生的人数是{num_a}，男生的比例是{num_a/unm_sum:.2%}')
print(f'女生的人数是{num_b}，女生的比例是{num_b/unm_sum:.2%}')
