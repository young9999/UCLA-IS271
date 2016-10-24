'''
Extra Credit 2 - Linked Lists

Name: 
'''


class Node():

	def __init__(self, value):
		self.value = value
		self.next = None
		self.prev = None


class Queue():

	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	def push(self, value):
		newNode = Node(value)
		newNode.next = None
		#self.Node = value
		if self.tail == None: #head
			self.head = newNode
			self.tail = newNode
		else:
			self.tail.next = newNode
			newNode.prev = self.tail
			self.tail = newNode
		self.length += 1

	def pop(self):
		temp = self.head.value
		self.head = self.head.next
		self.length -= 1
		if self.length == 0:
			self.last = None
		return temp

class Stack(Queue):

	def pop(self):
		temp = self.tail.value
		self.tail = self.tail.prev
		if self.tail == None:
			self.head = None
		else:
			self.tail.next = None
		self.length -= 1
		return temp
