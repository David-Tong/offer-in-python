class Solution(object):
    def dicesProbability(self, n):
        """
        :type n: int
        :rtype: List[float]
        """
        N = 6 * n + 1
        dp = [[0] * N for _ in range(n + 1)]
        dp[0][0] = 1

        for x in range(n):
            for y in range(N - 1, 0, -1):
                for z in range(6):
                    if y - z - 1 >= 0:
                        dp[x + 1][y] += dp[x][y - z - 1]

        ans = list()
        for x in dp[n]:
            if x > 0:
                ans.append(x * 1.0 / (6 ** n))
        return ans


n = 1
n = 2
n = 3
n = 11

solution = Solution()
print(solution.dicesProbability(n))
