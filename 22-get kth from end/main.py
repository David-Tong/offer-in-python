# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        curr = head
        curr2 = head

        idx = 0
        while idx < k:
            if curr:
                curr = curr.next
            else:
                return None
            idx += 1

        while curr:
            curr = curr.next
            curr2 = curr2.next
        return curr2


node = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

k = 2
k = 12

solution = Solution()
head = solution.getKthFromEnd(node, k)

head
