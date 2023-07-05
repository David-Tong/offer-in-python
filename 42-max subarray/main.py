class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        presum = 0
        ans = float("-inf")
        for num in nums:
            if presum < 0:
                presum = 0
            presum += num
            ans = max(ans, presum)
        return ans


nums = [-2,1,-3,4,-1,2,1,-5,4]

solution = Solution()
print(solution.maxSubArray(nums))
