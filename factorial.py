#!/usr/bin/env python

def fact1(n):
	if n == 0:
		return 1
	else:
		return n*fact1(n-1)

print fact1(50)
print fact1(5)
print fact1(0)
#print fact(50)


def fact2(n):
	summ = 1
	if n == 0:
		return summ
	else: 
		while n>0:
			summ = summ * n
			n -= 1
	return summ

print fact2(50)
print fact2(5)
print fact2(0)
#print fact(50)
