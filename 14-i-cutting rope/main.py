class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 1

        N = n + 1
        dp = [0] * N
        dp[2] = 1

        for x in range(3, N):
            for y in range(2, x):
                dp[x] = max(dp[x], max(y * (x - y), y * dp[x - y]))
        return dp[n]


n = 2
n = 10
n = 58

solution = Solution()
print(solution.cuttingRope(n))
