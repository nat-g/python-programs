#!/usr/bin/env python

class Node(object):

	def __init__(self, value):
		self.value = value
		self.nextnode = None


def countnodes(node):

	if node.isEmpty:
		return False
	else:
		count = 1
		while node.nextnode:
			count += 1
			node = node.nextnode

	return count


def last_to_the_end(n,node):
	
	number = countnodes(node)
	targetN = number - n + 1

	while targetN > 0:
		node = node.nextnode
		targetN -= 1

	return node


def nth_to_the_last_node(n,node):
	left_pointer = head
	right_pointer = head

	# set the right pointer n nodes away from the head
	for i in xrange(n-1):

		#check for edge case if not enough nodes
		if not right_pointer.nextnode:
			raise LookupError('Error: n is larger than the linked list')

		right_pointer = right_pointer.nextnode

	while right_pointer.nextnode:

		left_pointer = left_pointer.nextnode
		right_pointer = right_pointer.nextnode

	return left_pointer




a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e
target_node = nth_to_the_last_node(2,a)

print target_node.value
