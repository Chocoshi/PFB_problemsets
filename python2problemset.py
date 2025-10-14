#!/usr/bin/env python3
color ='beautiful green'
if 'green' in color:
	print('Yes indeed')
else:
	print('Nope')
number = -99
if number > 0:
	print(number, "is positive")
if number < 0:
	print(number, "is negative")
number1 = 88
if number1 > 0:
	print(number1, "is positive")
elif number1 == 0:
	print(number1, "is zero")
else:
	print(number1, "is negative")
number2 = 888
if number2 > 0:
	print(number2, "is positive")
	if number2 < 50:
		print(number2, "is less than 50")
		if number2 % 2 == 0:
			print(number2, "it is an even number that is smaller than 50")
	else:
		print(number2, "is more than 50")
		if number2 % 3 == 0:
			print(number2, "it is larger than 50 and divisible by 3")
		if number2 % 2 == 0:
			print(number2, "is even")
		 
