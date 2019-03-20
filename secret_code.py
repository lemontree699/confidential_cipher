import random

# 构建table 并分成不同的颜色区域
table = range(1,26)
table = set(table)

blue = random.sample(table, 8)
# print(blue)
table = table - set(blue)

red = random.sample(table, 9)
# print(red)
table = table - set(red)

black = random.sample(table, 1)
# print(black)
table = table - set(black)

yellow = random.sample(table, 7)
# print(yellow)
table = table - set(yellow)

# 画table
from turtle import *
import time

screensize(500, 500)
speed(100)

def square():
	forward(100)
	right(90)
	forward(100)
	right(90)
	forward(100)
	right(90)
	forward(100)
	right(90)

# time.sleep(5)

for i in range(1,6):
	for j in range(1,6):
		if (i-1)*5+j in red:
			fillcolor("red")
			begin_fill()
			penup()
			X = -250+100*(j-1)
			Y = 250-100*(i-1)
			goto(X, Y)
			pendown()
			square()
			end_fill()

		elif (i-1)*5+j in black:
			fillcolor("black")
			begin_fill()
			penup()
			X = -250+100*(j-1)
			Y = 250-100*(i-1)
			goto(X, Y)
			pendown()
			square()
			end_fill()
			
		elif (i-1)*5+j in blue:
			fillcolor("blue")
			begin_fill()
			penup()
			X = -250+100*(j-1)
			Y = 250-100*(i-1)
			goto(X, Y)
			pendown()
			square()
			end_fill()
			
		elif (i-1)*5+j in yellow:
			fillcolor("yellow")
			begin_fill()
			penup()
			X = -250+100*(j-1)
			Y = 250-100*(i-1)
			goto(X, Y)
			pendown()
			square()
			end_fill()
			
done()

# 读取词语库
with open ('./words.txt') as f:
	words = f.read().split()
	# print(words)
# 去除重复
words = set(words)
words = list(words)
words = random.sample(words, 25)

# 显示词语
def show(words):
	print('----------------------------------------')
	for i in range(5):
		for j in range(5):
			print('{:<9}\t'.format(words[i*5+j]),end = '')  # 采用左对齐 右图
		print('\n')
	print('----------------------------------------')

# main
print('\nGame begins, the vocabulary is as follows:\n')
show(words)

while 1:
	print('Which team do you belong to? r or b?')
	team = input()
	print('Please choose word.')
	word = input()
	index = words.index(word) + 1
	if index in red:
		if team == 'r':
			print('\nCongratulations!')
			words[index - 1] = '①①①'
			print('Now the table is:\n')
			show(words)
		elif team == 'b':
			print('\noops! You choose another team\'s words.')
			words[index - 1] = '①①①'
			print('Now the table is:\n')
			show(words)
	elif index in blue:
		if team == 'b':
			print('\nCongratulations!')
			words[index - 1] = '②②②'
			print('Now the table is:\n')
			show(words)
		elif team == 'r':
			print('\noops! You choose another team\'s words.')
			words[index - 1] = '②②②'
			print('Now the table is:\n')
			show(words)
	elif index in yellow:
		print('\nYou choose words that are not valid.')
		words[index - 1] = '〇〇〇'
		print('Now the table is:\n')
		show(words)
	elif index in black:
		print('boom!! You die.')
		break
