class Solution(object):
    def sumNums(self, n):
        """
        :type n: int
        :rtype: int
        """
        def doSum(n):
            total = n > 0 and n + doSum(n - 1)
            return total

        return doSum(n)


n = 3
n = 9
n = 10000

solution = Solution()
print(solution.sumNums(n))
