#!/usr/bin/env python3
user= int(input("Enter a Number less than 25"))

if user > 25:
	print("Error")
else:
	while user <= 25:
		print(user)
		user += 1

