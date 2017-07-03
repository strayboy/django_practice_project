#coding=utf-8
#创建单节点
class Node():
	def __init__(self,elem_):
		self.elem = elem_
		self.next = None

#创建单项循环列表
class SingleCycLinkList():
	def __init__(self,Node = None):
		self.__head = Node
		if Node:
			Node.next = Node

	def is_empty(self):#判断链表是否为空
		return self.__head is None
	

	def length(self):
		#返回链表的长度
		if self.is_empty():
			return 0

		cur = self.__head
		count = 1
		while cur.next != self.__head:
			count += 1
			cur = cur.next
		return count

	def travel(self):
		#遍历
		if self.is_empty():
			return

		cur = self.__head
		while cur.next != self.__head:
			print(cur.elem,end = ' ')
			cur = cur.next
		#退出循环，current指向尾部节点，但尾节点的元素未打印
		print(cur.elem)
		print()
			
	def add(self,item):
		#在头部添加一个节点,头插法
		scnode = Node(item)

		#判断空链表
		if self.is_empty():
			self.__head = scnode
			scnode.next = scnode
		else:
			#先找尾节点或者先插入头结点都可以
			cur = self.__head
			while cur.next != self.__head:
				cur = cur.next
			scnode.next = self.__head
			self.__head = scnode
			cur.next = scnode
			#cur.next = self.__head

	def append(self,item):
		#在尾部添加一个节点
		node = Node(item)

		if self.is_empty():
			self.__head = node
			node.next = node
		else:
			cur = self.__head
			while cur.next != self.__head:
				cur =cur.next
			node.next = cur.next#or self.__head
			cur.next = node
			'''
			cur.next = node
			node.next = self.__head
						'''

	def insert(self,pos,item):
		#在指定位置pos添加节点
		
		if pos <= 0:
			self.add(item)
		elif pos > (self.length()-1):
			self.append(item)
		else:
			node = Node(item)
			pre = self.__head
			count = 0
			while count < (pos-1):
				count += 1
				pre =pre.next

			node.next = pre.next
			pre.next = node


	def search(self,item):
		#查找节点是否存在
		if self.is_empty():
			return False
		cur = self.__head
		while cur.next != self.__head:
			if cur.elem == item:
				return True

			else:
				cur = cur.next
			#退出循环时，cur指向的是为节点，需要判断为节点的元素
			if cur.elem == item:
				return True
		return False


	def remove(self,item):
		#删除一个节点
		if self.is_empty():
			return

		cur = self.__head
		pre = None

		while cur.next != self.__head:
			if cur.elem == item:
				#先判断此节点是否是头结点
				if cur == self.__head:
					#先找尾部节点
					rear = self.__head
					while rear.next != self.__head:
						rear = rear.next
					self.__head = cur.next
					rear.next = self.__head
				else:#中间节点
					pre.next = cur.next   #对于尾部节点不包含
				return #不能用break，否则退出了整个函数
			else:
				pre = cur
				cur = cur.next
		#退出循环，cur指向尾部节点
		if cur.elem == item:#判断是否是单个节点，是否只有一个节点
			if cur == self.__head: # pre == None
				self.__head = None
			else:
				pre.next = cur.next


		'''
		循环链表的删除：
		头结点、尾部节点、中间节点、单个节点（一个）
		'''

if __name__ == "__main__":
    ll = SinCycLinkedlist()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    ll.insert(4, 5)
    ll.insert(0, 6)
    print "length:",ll.length()
    ll.travel()
    print ll.search(3)
    print ll.search(7)
    ll.remove(1)
    print "length:",ll.length()
    ll.travel()
