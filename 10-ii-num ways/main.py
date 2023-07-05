class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        MODULO = 10 ** 9 + 7
        N = 101
        dp = [0] * N
        dp[0] = 1
        dp[1] = 1

        for x in range(2, N):
            dp[x] = dp[x - 1] + dp[x - 2]
        return dp[n] % MODULO


n = 2
n = 7
n = 0
n = 100

solution = Solution()
print(solution.numWays(n))
