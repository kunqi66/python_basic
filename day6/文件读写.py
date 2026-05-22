fw = open('.\\document\\python1.txt',mode='r+',encoding='utf-8')
fw1 = open('.\\document\\copy_python1.txt',mode='w',encoding='utf-8')
data = fw.read(1024)
while data:
    fw1.write(data)
    data = fw.read()
fw.close()
fw1.close()