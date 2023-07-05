class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def binary(pow):
            bins = list()
            while pow:
                if pow & 1:
                    bins.append(1)
                else:
                    bins.append(0)
                pow >>= 1
            return bins

        negative_n = False
        if n == 0:
            return 1
        elif n < 0:
            negative_n = True
            n = -1 * n

        bins = binary(n)
        L = len(bins)

        pows = [0] * L
        pows[0] = x
        for idx in range(1, L):
            pows[idx] = pows[idx - 1] * pows[idx - 1]

        ans = 1
        for idx in range(L):
            if bins[idx] == 1:
                ans *= bins[idx] * pows[idx]

        if negative_n:
            return 1 * 1.0 / ans
        else:
            return ans


x = 2.00000
n = 10

x = 2.10000
n = 3

x = 2.00000
n = -2

x = 0
n = 3

x = 0.44528
n = 0

solution = Solution()
print(solution.myPow(x, n))
