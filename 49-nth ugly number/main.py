class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        from heapq import heapify, heappush, heappop
        heap = list()
        heapify(heap)
        heappush(heap, 1)
        from collections import defaultdict
        visited = defaultdict(bool)
        visited[1] = True

        for x in range(n):
            item = heappop(heap)
            for y in [2, 3, 5]:
                target = y * item
                if not visited[target]:
                    heappush(heap, item * y)
                    visited[target] = True
        return item


n = 10
#n = 20
#n = 1690

solution = Solution()
print(solution.nthUglyNumber(n))