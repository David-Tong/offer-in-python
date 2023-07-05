# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def getLength(node):
            ans = 0
            while node:
                node = node.next
                ans += 1
            return ans

        lenA = getLength(headA)
        lenB = getLength(headB)

        if lenA < lenB:
            headA, headB = headB, headA
            lenA, lenB = lenB, lenA

        k = lenA - lenB
        nodeA = headA
        idx = 0
        while idx < k:
            nodeA = nodeA.next
            idx += 1

        nodeB = headB
        while nodeA != nodeB:
            nodeA = nodeA.next
            nodeB = nodeB.next

        return nodeA


