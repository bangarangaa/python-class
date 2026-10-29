#!/usr/bin/env python 3
table = 0

while table <=10:
	row = 0

	while row <= 10:

		print (f"{table * row}", end=" ")

		row = row + 1

	print ("\n")
	table = table + 1

