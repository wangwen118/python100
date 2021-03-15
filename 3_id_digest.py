'''
@2021/3/15
id | 性别 | 年龄 | 地名
要求: 打印 3.txt 文件中每行的ID列
进阶: 计算 3.txt 文件中每行的 id 列年龄列之和并打印, 提示需要把字符串转为数字
'''

import random

# with open('3.txt', 'w+') as f:
#     for i in range(140):
#         line = "%d | female | %d | yuping" % (i, random.randint(20, 40+i))
#         f.write(line+"\n")

# with open('./3.txt', 'r') as f:
#     for line in f:
#         id, _, age, _ = line.split('|')
#         sum = int(id) + int(age)
#         res = "%s + %s =  %s" % (id, age, sum)
#         print(res)

# 输出年龄在20-70之间的行
with open('./3.txt', 'r') as f:
    for line in f:
        id, sex, age, hometown = line.split('|')
        if int(age) > 20 and int(age) < 70:
            print(line)
