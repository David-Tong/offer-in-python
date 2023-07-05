class Solution(object):
    def dicesProbability(self, n):
        """
        :type n: int
        :rtype: List[float]
        """
        N = 6 * n + 1
        prev = [0] * N
        prev[0] = 1

        for x in range(n):
            curr = [0] * N
            for y in range(N - 1, 0, -1):
                for z in range(6):
                    if y - z - 1 >= 0:
                        curr[y] += prev[y - z - 1]
            prev = curr

        ans = list()
        for x in curr:
            if x > 0:
                ans.append(x * 1.0 / (6 ** n))
        return ans


n = 1
n = 2
n = 3
n = 11

solution = Solution()
print(solution.dicesProbability(n))
