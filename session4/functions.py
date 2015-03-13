#!/usr/bin/python

# def hello_world(languages_dict):
# 	print languages_dict

# languages = ["python", "Java"]
# languages_dict = {'lang':'python'}
# hello_world(languages_dict)

def convert_c_to_f(C):
	F = float(C) * (9/5) + 32
	print F

# c = raw_input("Enter C:")
# convert_c_to_f(c)

def add_two_numbers(n1, n2, op="add"):
	if op == "add":
		return n1+n2
	elif op == "multiply":
		return n1*n2

# result = add_two_numbers(10, 20, "multiply")
# print result

# if condition:
# 	statement
# elif condition:
# 	statement

# def return_list():
# 	L = [1,2,3]
# 	return L

# returned_list = return_list()
# print returned_list

