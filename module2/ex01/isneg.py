#!/usr/bin/env python3

user=input("Please enter a number")

if int(user)<0:
	print("This number is negative")

elif int(user)>0:
	print("This number is positive")
else:
	print("This number is both positive and negative")

