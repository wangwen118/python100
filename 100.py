# -*- coding:utf8 -*-

# 100
'''
	列表转换为字典
'''
# x = [1, 2]
# y = ['one', 'two']
# d = dict([y, x])
#print(d)

# 99
'''
	有两个文件磁盘A和B，各存放一行字母，
	要求把这两个文件中的信息合并，按照字母顺序排序，
	输出到一个磁盘文件C中
'''
# with open('C:/Users/yp_wa/Desktop/t1.txt', 'r') as f1, open('C:/Users/yp_wa/Desktop/t2.txt', 'r') as f2, open('C:/Users/yp_wa/Desktop/t3.txt', 'w') as f3:
# 	for a in f1:
# 		b = f2.read()
# 	c = list(a + b)
# 	c.sort()
# 	d = '\n'
# 	d = d.join(c)
# 	f3.write(d)

# 98
'''
	从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存
'''
# s = input('请输入一个字符串：')
# with open('t4.txt', 'w') as f:
# 	f.write(s.upper())

# 97?????????????????????????????????????????
'''
	从键盘输入一些字符，逐个把他们写到磁盘文件上，
	直到输入一个#为止
'''
# s = input('请输入字符：')
# d = '\n'

# with open('t5.txt', 'w') as f:
# 	while s != '#':
# 		d = d.join(s)
# 		f.write(d)

# 96
'''
	计算字符串中子串出现的次数
'''
# s = input('请输入一个字符串：')
# s1 = input('请输入一个子串：')
# c = s.count(s1)

# 95
'''
	字符串日期转换为易读的日期格式
'''
# from dateutil import parser
# dt = parser.parse("Aug 28 2015 12:00AM")
# print(dt) 

# 94????????????????????????????????????????????
'''
	一个猜数游戏，判断一个人反应快慢
'''
# if __name__ == '__main__':
#     import time
#     import random
    
#     play_it = input('do you want to play it.(\'y\' or \'n\')')
#     while play_it == 'y':
#         c = input('input a character:\n')
#         i = random.randint(0,2**32) % 100
#         print('please input number you guess:\n')
#         start = time.clock()
#         a = time.time()
#         guess = int(input('input your guess:\n'))
#         while guess != i:
#             if guess > i:
#                 print('please input a little smaller')
#                 guess = int(input('input your guess:\n'))
#             else:
#                 print('please input a little bigger')
#                 guess = int(input('input your guess:\n'))
#         end = time.clock()
#         b = time.time()
#         var = (end - start) / 18.2
#         print(var)
#         # print 'It took you %6.3 seconds' % time.difftime(b,a))
#         if var < 15:
#             print('you are very clever!')
#         elif var < 25:
#             print('you are normal!')
#         else:
#             print('you are stupid!')
#         print('Congradulations')
#         print('The number you guess is %d' % i)
#         play_it = input('do you want to play it.')

# 93
'''
	计算时间差
'''
# import time
# start = time.clock()
# for i in range(100):
# 	print(i)
# end = time.clock()
# print('diff is %6.3f' % (end - start))

# 92
# import time
# start = time.time()
# for i in range(100):
# 	print(i)
# end = time.time()
# print('diff is %f' % (end - start))

# 89????????????????????????????????????????????????????????????????????????????????????
'''
	某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，
	加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换
'''
# from sys import stdout
# if __name__ == '__main__':
# 	a = int(input('请输入四位整数：/n'))
# 	aa = []
# 	aa.append(a % 10)
# 	aa.append(a % 100 / 10)
# 	aa.append(a % 1000 / 100)
# 	aa.append(a / 1000)
	 
# 	for i in range(4):
# 		aa[i] += 5
# 	    aa[i] %= 10
# 	for i in range(2):
# 		aa[i], aa[3 - i] = aa[3 - i], aa[i]
# 	for i in range(3,-1,-1):
# 		stdout.write(str(aa[i]))

# 88
'''
	读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊
'''
# i = 1

# while i <= 7:
# 	x = int(input('请输入一个整数：\n'))
# 	while x < 50 or x > 1:
# 		x = int(input('请输入一个整数：\n'))
# 	print(x * '*')
# 	i += 1

# 85????????????????????????????????????????????????
'''
	输入一个奇数，然后判断最少几个 9 除于该数的结果为整数
'''



# 81
'''
	809*??=800*??+9*?? 其中??代表的两位数, 809*??为四位数，8*??的结果为两位数，9*??的结果为3位数。求??代表的两位数，及809*??
'''
# a = 809
# for i in range(10,100):
#     b = i * a
#     if b >= 1000 and b <= 10000 and 8 * i < 100 and 9 * i >= 100:
#         print(b,' = 800 * ', i, ' + 9 * ', i)

# 80
'''
	海滩上有一堆桃子，五只猴子来分。
	第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，拿走了一份。
	第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，
	第三、第四、第五只猴子都是这样做的，问海滩上原来最少有多少个桃子？
'''


# 79
'''
	字符串排序
'''
# a = input('请输入字符串：')
# b = input('请输入字符串：')
# c = input('请输入字符串：')

# if a > b:
# 	a, b = b, a
# if b > c:
# 	b, c = c, b
# if a > c:
# 	a, c = c, a
# print(a, b, c)

# 78
'''
	找到年龄最大的人，并输出
'''
# person = {
# 	"wangwen": 24,
# 	"liuwei": 25,
# 	"liuyang": 26
# }
# max_age = 0
# for k,v in person.items():
# 	if v > max_age:
# 		v, max_age = v, max_age
# 		name = k
# print('年龄最大的是%s,年龄是%d' % (k, v)) 

# 76
'''
	编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
'''
# def odd(n):
# 	s = 0.0
# 	i = 0.0
# 	for i in range(1,n+1):
# 		if i%2 != 0:
# 			s += 1.0/i
# 	return s

# def even(n):
# 	for i in range(2,n):
# 		if i%2 == 0:
# 			s += 1.0/i
# 	return s

# def f(fn,n):
# 	s = fn(n)
# 	return s

# if __name__ == '__main__':
# 	n = int(input('请输入一个数字：'))
# 	sum = f(odd, n)
# 	print(sum)

# 73
'''
	反向输出一个链表
'''
# s = []
# for i in range(6):
# 	i = int(input('请输入一个数字：'))
# 	s.append(i)
# s.reverse()
# print(s) 

# 70
'''
	写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度
'''
# def length(n):
# 	s = len(n)
# 	return s

# if __name__ == '__main__':
# 	n = input('请输入一个字符串:')
# 	l = length(n)
# 	print(l)

# 70
'''
	写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度
'''
# if __name__ == '__main__':
# 	s = input('please input a string:')
# 	print('the length of string is %d' % len(s))

# 69
'''
	有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位
'''
