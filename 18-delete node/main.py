# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head

        prev = dummy
        curr = head

        while curr and curr.val != val:
            prev = curr
            curr = curr.next

        if curr:
            prev.next = curr.next

        return dummy.next


node = ListNode(4)
node2 = ListNode(5)
node3 = ListNode(1)
node4 = ListNode(9)

node.next = node2
node2.next = node3
node3.next = node4

val = 5
val = 4
val = 9
val = 11
val = -1

solution = Solution()
head = solution.deleteNode(node, val)

head