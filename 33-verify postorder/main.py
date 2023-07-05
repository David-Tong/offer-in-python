class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        def verify(postorder):
            if len(postorder) <= 1:
                return True

            lessRoot = True
            root = postorder[-1]
            rightStart = -1
            for idx, num in enumerate(postorder[:-1]):
                if num > root:
                    if lessRoot:
                        rightStart = idx
                        lessRoot = False
                elif num < root:
                    if not lessRoot:
                        return False

            return verify(postorder[:rightStart]) & verify(postorder[rightStart:-1])

        return verify(postorder)


postorder = [1,6,3,2,5]
postorder = [1,3,2,6,5]
postorder = [1]

solution = Solution()
print(solution.verifyPostorder(postorder))
