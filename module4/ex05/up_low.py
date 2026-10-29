#!/usr/bin/env python3

text= input("Enter a string: ")

result = ""

for letter in text:
	if letter== letter.upper():
		result = result + letter.lower()
	else:

		result = result + letter.upper()

print (result)
