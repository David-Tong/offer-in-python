class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        target = n
        ans = 0
        while target:
            if target & 1:
               ans += 1
            target >>= 1
        return ans


n = 11
n = 128
n = 4294967293

solution = Solution()
print(solution.hammingWeight(n))
