import re

file_name = "4_1_testFile.txt"
f = open(file_name,'w', encoding='utf-8')
f.write('中华人民共和国中国人民')
# 换行符
f.write('\n')
# 关闭文件
f.close()

fo = open("5_1_testFile.txt",'r+',encoding='utf-8').read()
print(fo.count("中国"))

