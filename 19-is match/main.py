class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        M = len(s)
        N = len(p)

        # dp[x][y] - whether s[:x] and p[:y] is match
        dp = [[False] * (N + 1) for _ in range(M + 1)]

        for x in range(M + 1):
            for y in range(N + 1):
                if x == 0 and y == 0:
                    dp[x][y] = True
                    continue

                # x > 0 and y == 0
                if y == 0:
                    dp[x][y] = False
                    continue

                # case 1 - regular char or "."
                if y > 0 and p[y - 1] != "*":
                    if x > 0 and (s[x - 1] == p[y - 1] or "." == p[y - 1]):
                        dp[x][y] |= dp[x - 1][y - 1]
                else:
                    # case 2 - for "*" but "c*" not used
                    if y > 1:
                        dp[x][y] |= dp[x][y - 2]

                    # case 3 - "c*" used
                    if (x > 0 and y > 1) and (s[x - 1] == p[y - 2] or "." == p[y - 2]):
                        dp[x][y] |= dp[x - 1][y]
        return dp[M][N]


s = "aa"
p = "a"

s = "aa"
p = "a*"

s = "ab"
p = ".*"

s = "aaaa"
p = "a*b*"

s = "abbcca"
p = ".*"

s = "abbcca"
p = "ab*c*."
p = "ab*.*"

s = ""
p = ".*"

s = ""
p = "."

solution = Solution()
print(solution.isMatch(s, p))
