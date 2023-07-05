class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        MODULO = 10 ** 9 + 7

        if n < 3:
            return 1
        elif n == 3:
            return 2

        MOD3 = n // 3
        for x in range(MOD3, -1, -1):
            remain = n - 3 * x
            if remain % 2 == 0:
                y = remain // 2
                break

        ans = 3 ** x * 2 ** y % MODULO
        return ans


n = 2
n = 3
#n = 5
#n = 10
#n = 20
#n = 1000

solution = Solution()
print(solution.cuttingRope(n))
