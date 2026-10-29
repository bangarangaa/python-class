#!/usr/bin/env python3
number=int(input("Give me the first Number: "))
number2=int(input("Give me the second Number: "))

print ("Thank you!")

print (f"{number} + {number2} = {number+number2}")

print (f"{number} - {number2} = {number-number2}")

if number2 !=0:
	print (f"{number}/{number2}={number/number2}")
else:
	print ("Cannot divide with zero")

print (f"{number} * {number2} = {number * number2}")
