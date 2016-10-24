import unittest

from linkedlist import Queue, Stack


class TestQueue(unittest.TestCase):

	def test_push(self):
		q = Queue()
		q.push('A')
		self.assertEqual(q.length, 1)
		q.push('B')
		self.assertEqual(q.length, 2)

	def test_pop(self):
		q = Queue()
		for num in range(1, 6):
			q.push(num)
		exp_len = 5
		self.assertEqual(q.length, exp_len)
		for num in range(1, 6):
			value = q.pop()
			exp_len -= 1
			self.assertEqual(value, num)
			self.assertEqual(q.length, exp_len)


class TestStack(unittest.TestCase):

	def test_push(self):
		s = Stack()
		s.push('A')
		self.assertEqual(s.length, 1)
		s.push('B')
		self.assertEqual(s.length, 2)

	def test_pop(self):
		s = Stack()
		for num in range(1, 6):
			s.push(num)
		exp_len = 5
		self.assertEqual(s.length, exp_len)
		for num in range(5, 0, -1):
			value = s.pop()
			exp_len -= 1
			self.assertEqual(value, num)
			self.assertEqual(s.length, exp_len)


if __name__ == "__main__":
	unittest.main()