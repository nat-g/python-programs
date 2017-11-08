#!/usr/bin/env python

"""
We have a list of integers, where:

The integers are in the range 1..n1..n
The list has a length of n+1n+1
It follows that our list has at least one integer which appears at least
 twice. But it may have several duplicates, and each duplicate may appear
 more than twice.

Write a function which finds an integer that appears more than once in 
our list. (If there are multiple duplicates, you only need to find one 
of them.)

We're going to run this function on our new, super-hip Macbook Pro 
With Retina Display™. Thing is, the damn thing came with the RAM 
soldered right to the motherboard, so we can't upgrade our RAM. 
So we need to optimize for space!
"""

"""

#if sorted

def duplicate(list):
	previous = ""
	duplicates = []
	for i in list:
		print "for loop: {}".format(i)
		if i != previous:
			found = False
			previous = i
		elif i == previous:
			found = True
			duplicates.append(i)

	return duplicates
"""

#This one's a classic! We just do one walk through the list, 
#using a set to keep track of which items we've seen!
#O(n) time and ... O(n) space
def find_repeat(numbers):
    numbers_seen = set()
    for number in numbers:
        if number in numbers_seen:
            return number
        else:
            numbers_seen.add(number)
    # whoops--no duplicate
    raise Exception('no duplicate!')

#We can "brute force" this by taking each number in the 
#range 1..n and, for each, walking through the list to see 
#if it appears twice.
#This is O(1) space and O(n^2) time.
def find_repeat_brute_force(numbers):
	for needle in range(1, len(numbers)):
		has_been_seen = False
		for number in numbers:
			if number == needle:
				if has_been_seen:
					return number
				else:
					has_been_seen = True

    # whoops--no duplicate
	raise Exception('no duplicate!')

"""
One way to beat O(n^2) time is to get O(nlgn) time. 
Sorting takes O(nlgn) time. And if we sorted the list, 
any duplicates would be right next to each-other!
But if we start off by sorting our list we'll need to take O(n) space 
to store the sorted list..unless we sort the input list in place.
Steps:
-Do an in-place sort of the list (for example an in-place mergesort).
-Walk through the now-sorted list from left to right.
-Return as soon as we find two adjacent numbers which are the same.
This'll keep us at O(1) space and bring us down to O(nlgn) time.
"""



ex_list = [1,2,5,5,7,9,9,10,11,33,33]
#print duplicate(ex_list)
print find_repeat_brute_force(ex_list)
