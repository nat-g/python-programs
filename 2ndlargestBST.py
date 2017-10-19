#!/usr/bin/env python

class BinaryTree():

	def __init__(self, value):
		self.key = value
		self.left = None
		self.right = None

	def insertRight(self,value):
		self.right = value
		return self.right

	def insertLeft(self,value):
		self.left = value
		return self.left

#Find largest. This is a helper function for find_second_largest.
def find_largest(root):
	current = root
	while root.right:
		current = root.right
	return current

#We can also find the second largest in one walk down the tree. 
#At each step, we have a few cases:
def find_second_largest(root):
	#If root node is None or only one root node exists
	if root is None or (root.right is None and root.left is None):
		print "Tree has to have at least 2 nodes"
	#If root has only left child (left subtree) and no right child (right subtree)
	#If root has a right child, but right child has no right child,
	#but only a left child
	if root.left and not root.right:
		find_largest(root.left)
	#If root has a right child but that child has no children, 
	#then the root is the second lagest
	if root.right and not root.right.right and not root.right.left:
		return root.key
	#We've left with the case when root has a right child, and that 
	#right child has a child
	find_second_largest(root.right)


"""
If we're using recursion:
It'll take O(h) time (where h is the height of the tree) and O(h) space.
In recursive functions, the stack can get as tall as the number of times the 
function calls itself. This can cause a problem: the stack has a limited amount 
of space, and if it gets too big you can get a stack overflow error.
"""

"""
If we're using while loop:
We're doing one walk down our BST, which means O(h) time, where h is the 
height of the tree (again, that's O(lgn) if the tree is balanced, 
O(n) otherwise). O(1) space.
"""

root_1 = BinaryTree(4)
root_1.left = BinaryTree(2)
root_1.right = BinaryTree(5)
root_1.left.left = BinaryTree(1)
root_1.left.right = BinaryTree(3)

print find_second_largest(root_1)

import unittest

class TestBst(unittest.TestCase):
    def test_none(self):
        self.assertTrue(find_second_largest(None))

if __name__ == '__main__':
    unittest.main()
