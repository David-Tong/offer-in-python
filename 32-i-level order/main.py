# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        from collections import deque
        bfs = deque()
        if root:
            bfs.append(root)

        ans = list()
        while bfs:
            size = len(bfs)
            for x in range(size):
                node = bfs.popleft()
                ans.append(node.val)
                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)
        return ans


