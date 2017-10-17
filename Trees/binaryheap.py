#!/usr/bin/env python

"""
A binary heap will allow us both enqueue and dequeue items in O(logn)O(log⁡n).
The binary heap has two common variations: the min heap, in which the smallest
key is always at the front, and the max heap, in which the largest key value
is always at the front.
"""

class BinHeap:
	def __init__(self):
		self.heaplist = [0]
		self.currentsize = 0

	def percUp(self,i):
		while i // 2 > 0:
			if self.heapList[i] < self.heapList[i // 2]:
				tmp = self.heapList[i // 2]
				self.heapList[i // 2] = self.heapList[i]
				self.heapList[i] = tmp
			i = i // 2

#for insertion we need percUp function
	def insert(self,k):
		self.heaplist.append(k)
		self.currentsize = self.currentsize + 1
		self.percUp(self.currentsize)

	def percDown(self,i):
		while (i * 2) <= self.currentSize:
			mc = self.minChild(i)
			if self.heapList[i] > self.heapList[mc]:
				tmp = self.heapList[i]
				self.heapList[i] = self.heapList[mc]
				self.heapList[mc] = tmp
			i = mc

	def minChild(self,i):
		if i * 2 + 1 > self.currentSize:
			return i * 2
		else:
			if self.heapList[i*2] < self.heapList[i*2+1]:
				return i * 2
			else:
				return i * 2 + 1

# for delMin we need percDown and minChild fuctions
	def delMin(self):
		retval = self.heapList[1]
		self.heapList[1] = self.heapList[self.currentSize]
 		self.currentSize = self.currentSize - 1
		self.heapList.pop()
		self.percDown(1)
		return retval

	def buildHeap(self,alist):
		i = len(alist) // 2
		self.currentSize = len(alist)
		self.heapList = [0] + alist[:]
		while (i > 0):
			self.percDown(i)
			i = i - 1



bh = BinHeap()
bh.buildHeap([9,5,6,2,3])

print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())