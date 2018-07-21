# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def recursive(self,level,r1,r2):
        if level<=self.level:
            tail,up=self.recursive(level+1,r1.next,r2)
            ss=r1.val+up
            node = ListNode(ss % 10)
            node.next = tail
            return node, ss // 10
        else:
            ss=r1.val+r2.val
            if r1.next==None and r2.next==None:
                return ListNode(ss%10),ss//10
            tail,up=self.recursive(level+1,r1.next,r2.next)
            ss+=up
            node=ListNode(ss % 10)
            node.next=tail
            return node, ss // 10

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        len1=0
        len2=0
        a1=l1
        a2=l2
        while a1:
            len1+=1
            a1=a1.next
        while a2:
            len2+=1
            a2=a2.next
        if len1<len2:
            l1,l2=l2,l1
            len1,len2=len2,len1
        self.level=len1-len2
        tail,up=self.recursive(1,l1,l2)
        if up==0:
            return tail
        else:
            node=ListNode(up)
            node.next=tail
            return node
