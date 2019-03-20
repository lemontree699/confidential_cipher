import random

table = range(1,26)
table = set(table)

blue = random.sample(table, 8)
print('blue:', blue)
table = table - set(blue)

red = random.sample(table, 9)
print('red:', red)
table = table - set(red)

black = random.sample(table, 1)
print('black:', black)
table = table - set(black)

yellow = random.sample(table, 7)
print('yellow:', yellow)
table = table - set(yellow)




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