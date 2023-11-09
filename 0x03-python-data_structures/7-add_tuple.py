#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
	tuple_1 = len(tuple_a)
	tuple_2 = len(tuple_b)

	if tuple_1 < 2:
		if tuple_1 == 0:
			tuple_a = 0,0
		else:
			tuple_a = tuple_a[0],0
	if tuple_2 < 2:
		if tuple_2 == 0:
			tuple_b = 0,0
		else:
			tuple_b = tuple_b[0],0
	tuple_c =  tuple_a[0] + tuple_b[0],tuple_a[1] + tuple_b[1]
	return(tuple_c)
