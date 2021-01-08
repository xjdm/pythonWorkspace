import re

file_name = "4_2_testFile.txt"
f = open(file_name,'w', encoding='utf-8')
arr=['清华大学','北京大学','中国人民大学','北京航天大学','北京师范大学']
for value in arr:
    f.write(value)
    # 换行符
    f.write('\n')
f.close()

with open('4_2_testFile_bak.txt', 'w+', encoding='utf-8') as output, open('4_2_testFile.txt', 'r', encoding='utf-8') as input:
    output.write(input.read())
