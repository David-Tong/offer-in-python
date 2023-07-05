# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        node = head
        ans = list()
        while node:
            ans.append(node.val)
            node = node.next
        return ans[::-1]
