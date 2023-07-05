class Solution(object):
    def singleNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for num in nums:
            xor ^= num

        bit = 0
        while (xor >> bit) & 1 == 0:
            bit += 1

        num1, num2 = 0, 0
        for num in nums:
            if (num >> bit) & 1:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]


nums = [4,1,4,6]
nums = [1,2,10,4,1,4,3,3]

solution = Solution()
print(solution.singleNumbers(nums))
