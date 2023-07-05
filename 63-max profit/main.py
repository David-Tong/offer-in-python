class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        L = len(prices)

        if L < 2:
            return 0

        # minis - from left to right
        minis = list()
        mini = float("inf")
        for price in prices:
            mini = min(mini, price)
            minis.append(mini)

        # maxis - from right to left
        maxis = list()
        maxi = float("-inf")
        for price in prices[::-1]:
            maxi = max(maxi, price)
            maxis.append(maxi)
        maxis = maxis[::-1]

        ans = float("-inf")
        for x in range(L):
            ans = max(ans, maxis[x] - minis[x])
        return ans


prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
prices = []

solution = Solution()
print(solution.maxProfit(prices))
