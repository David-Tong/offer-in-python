class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        L = len(pushed)

        stack = list()
        idx = 0
        idx2 = 0

        while idx2 < L:
            while (not stack or stack[-1] != popped[idx2]) and idx < L:
                stack.append(pushed[idx])
                idx += 1

            while stack and stack[-1] == popped[idx2]:
                stack.pop()
                idx2 += 1

            if idx2 < L:
                if idx == L and stack[-1] != popped[idx2]:
                    return False

        return True


pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]

#pushed = [1,2,3,4,5]
#popped = [4,3,5,1,2]

solution = Solution()
print(solution.validateStackSequences(pushed, popped))
