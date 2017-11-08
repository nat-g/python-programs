#!/usr/bin/env python

"""
Write a function for reversing a linked list. ↴ Do it in-place. ↴
Your function will have one input: the head of the list.
Your function should return the new head of the list.
"""

class LinkedListNode:

	def __init__(self, value):
		self.value = value
		self.next  = None

	def Reverse(self):
		current = self.head
		next = None
		previous = None

		while current: #Or while current != None
			next = current.next
			current.next = previous
			previous = current
			current = next

		self.head = previous

		return self.head


"""
O(n) time and O(1) space. We pass over the list only once, 
and maintain a constant number of variables in memory.
"""