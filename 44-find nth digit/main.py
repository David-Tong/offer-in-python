class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        from math import ceil
        N = 10

        target = n
        for x in range(N):
            mod = x * 9 * 10 ** (x - 1)
            if target > mod:
                target -= mod
            else:
                xth = int(ceil(target / x))
                yth = int(target % x)
                break

        ans = xth + 10 ** (x - 1) - 1
        return str(ans)[yth - 1]


n = 3
n = 18
n = 2889
n = 2887

solution = Solution()
print(solution.findNthDigit(n))
