class Solution:
    def getMoneyAmount(self, n: 'int') -> 'int':
        memo = {}

        def f(lo, hi):
            if (lo, hi) not in memo:
                if lo >= hi:
                    return 0
                min1 = float("inf")
                for i in range(lo, hi):
                    res = i + max(f(lo, i - 1), f(i + 1, hi))
                    min1 = min(res, min1)
                memo[lo, hi] = min1
            return memo[lo, hi]

        r = f(1, n)
        return r


# class Solution:
#     class Solution:
#         def getMoneyAmount(self, n: 'int') -> 'int':
#
#             dp = [[0 for _ in range(n)] for _ in range(n)]
#
#             for i in range(1, n+1):
#                 for j in range

a = Solution()
b = a.getMoneyAmount(10)
print(b)