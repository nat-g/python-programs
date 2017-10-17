#!/usr/bin/env python
from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree
import operator

"""
Parsing mathematical expression.
Rules:
-If the current token is a '(', add a new node as the left child of the current node, and descend to the left child.
-If the current token is in the list ['+','-','/','*'], set the root value of the current node to the operator represented by the current token. Add a new node as the right child of the current node and descend to the right child.
-If the current token is a number, set the root value of the current node to the number and return to the parent.
-If the current token is a ')', go to the parent of the current node.

A simple solution to keeping track of parents as we traverse the tree 
is to use a stack. Whenever we want to descend to a child of the current 
node, we first push the current node on the stack. When we want to return 
to the parent of the current node, we pop the parent off the stack.
"""

#fpexp (type str) is our initial statement to parse

def buildParseTree(fpexp):
	fplist = fpexp.split()  #splitting a string of expression into list 
	#(type list)
	pStack = Stack()  #create empty stack 
	#(type 'instance')
	eTree = BinaryTree('')  #top root value 
	#(type 'instance')
	pStack.push(eTree)  #pushed current root into the stack
	print pStack.size()
	currentTree = eTree  #current position at a time
	#(type 'instance')

	for i in fplist:
		if i == '(':
			currentTree.insertLeft('') #inserts an empty node as a leftChild
			#print currentTree
			pStack.push(currentTree) #pushes current tree into the stack
			print 'StackSize: {},  root: {}      iteration(push): {} '.format(pStack.size(), currentTree.getRootVal(), i)
			currentTree = currentTree.getLeftChild() #sets current position to the leftChild

		elif i not in ['+', '-', '*', '/', ')']:
			print '-----before root: {} '.format(currentTree.getRootVal())
			currentTree.setRootVal(int(i))  #we are located at the node so set  the root value to the number 
			#parent = pStack.pop()  #???
			#print 'StackSize: {},  parent: {}     iteration(pop): digits'.format(pStack.size(), parent.getRootVal())
			#currentTree = parent  #this sets the current position to the parent node
			currentTree = pStack.pop()
			print 'StackSize: {},     iteration(pop): digits'.format(pStack.size())
			print '-----after root: {} '.format(currentTree.getRootVal())

		elif i in ['+', '-', '*', '/']:
			currentTree.setRootVal(i) #set the value to the operator for "currentTree"
			currentTree.insertRight('')  # descend to the right child
			pStack.push(currentTree) #push the new tree to the stack (will it push last updated node or the whole tree? Will it souble it?)
			print 'StackSize: {}, root: {}      iteration(push): {}'.format(pStack.size(), currentTree.getRootVal(), i)
			currentTree = currentTree.getRightChild()  # this set the current position to the rightChild

		elif i == ')':
			currentTree = pStack.pop()
			print 'StackSize: {}, root: {}      iteration(pop)'.format(pStack.size(), currentTree.getRootVal(), i)

		else:
			raise ValueError
	print 'eTee root:  {} '.format(eTree.getRootVal())
	return eTree


def evaluate(parseTree):
	opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

	leftC = parseTree.getLeftChild()
	rightC = parseTree.getRightChild()

	if leftC and rightC:
		fn = opers[parseTree.getRootVal()]
		return fn(evaluate(leftC),evaluate(rightC))
	else:
		return parseTree.getRootVal()


pt = buildParseTree("( ( 10 + 5 ) * 3 )")
print '-----------------'
pt.postorder() 
print '-----------------'
pt.preorder()  
print '-----------------'
pt.inorder()
print '-----------------'
print evaluate(pt)




