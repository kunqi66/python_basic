print('第一题')
def count_words_in_file(filename):
    fr = open(filename,mode='r',encoding='utf-8')
    ans = fr.readlines()
    num = 0
    for item in ans:
        num += len(item.split(' '))
    fr.close()
    return num
print(count_words_in_file('.\\晨练文件\\1.txt'))

print('='*100)
print('第二题')
tabl = {'zhangsan':'123456','qikun':'138356786763','wenq':'133456786543'}
def save_contacts(contacts, filename):
    fw = open(filename,mode='w',encoding='utf-8')
    for item in contacts.items():
        fw.write(f'{item[0]}:{item[1]}\n')
    fw.close()

def load_contacts(filename):
    fr = open(filename,mode='r',encoding='utf-8')
    ans = {}
    ans_lines = fr.readlines()
    for item in ans_lines:
        data = item.split(' ')[0][:-1].split(':')
        ans[data[0]] = data[1]
    fr.close()
    return ans

save_contacts(tabl , '.\\晨练文件\\2.txt')
print(load_contacts('.\\晨练文件\\2.txt'))

print('='*100)
print('第三题')
def count_log_levels(filename):
    fr = open(filename, mode='r', encoding='utf-8')
    lst = fr.readlines()
    ans = {}
    for item in lst:
        data = item.split('-')[3].strip()
        if data in ans:
            ans[data]+=1
        else:
            ans[data]=1
    fr.close()
    return ans
print(count_log_levels('.\\晨练文件\\log.txt'))