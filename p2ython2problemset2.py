#!/usr/bin/env python3
import sys
number1 = int(sys.argv[1])
number2 = int(sys.argv[2])
number3 = int(sys.argv[3])

if number1 > 0:
	print (number1, "positive")
	if number1 < 50:
		print (number1, "positive and less than 50")
		if number1 % 2 == 0:
			print (number1, "it is an even number that is smaller than 50")
	elif number1 > 50:
		print (number1, "larger than 50")
		if number1 % 3 == 0:
			print (number1, "it is larger than 50 and divisible by 3")
elif number1 < 0:
	print (number1, "negative")
elif number1 == 0:
	print (number1, "is zero")


