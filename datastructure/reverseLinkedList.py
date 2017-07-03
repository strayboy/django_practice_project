# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#思路：从一个表的首端不断取下节点，将其加入另一个表的首端
#对于单链表，在首端插入、删除节点是最方便的，O（1）时间

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newHead = None
        while head:
            cur = head
            head = head.next
            cur.next = newHead
            newHead = cur
        
        return newHead
            
            
        