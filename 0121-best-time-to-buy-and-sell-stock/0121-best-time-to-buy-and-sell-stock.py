class Solution:

    # Time Complexity: O(n) - We iterate through the prices array once
    # Space Complexity: O(1)


    def maxProfit(self, prices: List[int]) -> int:
        # keep track of best profit
        # sliding window -> move left pointer if next is smaller
        # swap left and right pointer if right is less than left 
        # our right point

        left, maxProf = 0, float("-inf")
        for i, price in enumerate(prices):
            maxProf = max(maxProf, prices[i] - prices[left])
            if prices[i] < prices[left]:
                left = i
        return maxProf

        