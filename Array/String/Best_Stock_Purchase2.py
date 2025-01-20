"""
122. Best Time to Buy and Sell Stock II
Difficulty: Medium

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time, 
but you can buy it and immediately sell it on the same day.

The goal is to find and return the maximum profit you can achieve.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation:
- Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5 - 1 = 4.
- Buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6 - 3 = 3.
- Total profit = 4 + 3 = 7.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation:
- Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5 - 1 = 4.
- Total profit = 4.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation:
- No transactions result in a positive profit, so the maximum profit is 0.

Constraints:
- 1 <= prices.length <= 3 * 10^4
- 0 <= prices[i] <= 10^4
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        earnings = 0
        current = prices[0]
        for i in prices:
            if current<i:
                earnings+=i-current
                current = i
            else:
                current = i
        return earnings