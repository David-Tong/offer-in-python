# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """
        def isSame(root, root2):
            if root and root2:
                if root.val != root2.val:
                    return False

            if (root and not root2) or (not root and root2):
                return False

            if not root and not root2:
                return True

            if isSame(root.left, root2.left) or isSame(root.right, root2.right):
                return True
            else:
                return False

        def search(root):
            if not root:
                return False

            if isSame(root, B):
                return True

            if search(root.left):
                return True

            if search(root.right):
                return True

            return False

        return search(A)


"""
node11 = TreeNode(3)
node12 = TreeNode(4)
node13 = TreeNode(5)
node14 = TreeNode(1)
node15 = TreeNode(2)

node11.left = node12
node11.right = node13
node12.left = node14
node12.right = node15

node21 = TreeNode(4)
node22 = TreeNode(1)

node21.left = node22
"""

node11 = TreeNode(1)
node12 = TreeNode(2)
node13 = TreeNode(3)

node11.left = node12
node11.right = node13

node21 = TreeNode(3)
node22 = TreeNode(1)

node21.left = node22

solution = Solution()
print(solution.isSubStructure(node11, node21))
