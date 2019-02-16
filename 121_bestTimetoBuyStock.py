class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        Mx = 0
        Mn = float("inf")

        for i in range(prices):
            Mn = min(Mn, prices[i])
            Mx = max(Mx, prices[i] - Mn)

        return Mx