"""
LeetCode Problem 121: Best Time to Buy and Sell Stock
Difficulty: Easy
Category: Arrays & Dynamic Programming
URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing
a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve
any profit, return 0.
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Approach: One Pass (Dynamic Programming)

        We track the minimum price seen so far and calculate the maximum profit
        we can get by selling at the current price.

        Time Complexity: O(n) - Single pass through the array
        Space Complexity: O(1) - Constant space used

        Key Insights:
        - We only need to track the minimum price and maximum profit
        - We can't sell before we buy, so we always look for minimum price before current day
        - This is a classic example of dynamic programming with state tracking
        """
        if not prices or len(prices) < 2:
            return 0

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # Update minimum price seen so far
            if price < min_price:
                min_price = price

            # Calculate potential profit if we sell at current price
            profit = price - min_price

            # Update maximum profit
            if profit > max_profit:
                max_profit = profit

        return max_profit

    def maxProfit_brute_force(self, prices: List[int]) -> int:
        """
        Alternative Approach: Brute Force

        Check all possible buy-sell pairs. Demonstrates why the one-pass approach is better.

        Time Complexity: O(n²) - All pairs
        Space Complexity: O(1) - Constant space
        """
        max_profit = 0
        n = len(prices)

        for i in range(n):
            for j in range(i + 1, n):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit

        return max_profit

    def maxProfit_kadane(self, prices: List[int]) -> int:
        """
        Alternative Approach: Kadane's Algorithm on Differences

        Convert the problem to maximum subarray sum on price differences.
        This approach treats the problem as finding the maximum subarray sum
        of the differences between consecutive days.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not prices or len(prices) < 2:
            return 0

        max_current = 0
        max_so_far = 0

        for i in range(1, len(prices)):
            # Calculate price difference from previous day
            diff = prices[i] - prices[i - 1]

            # Apply Kadane's algorithm
            max_current = max(0, max_current + diff)
            max_so_far = max(max_so_far, max_current)

        return max_so_far


if __name__ == "__main__":
    # Simple example usage
    solution = Solution()

    # Example 1: Basic usage
    prices = [7, 1, 5, 3, 6, 4]
    result = solution.maxProfit(prices)
    print(f"Example 1 - prices: {prices}")
    print(f"One-pass approach result: {result}")

    # Example 2: Compare approaches
    result_bf = solution.maxProfit_brute_force(prices)
    result_kadane = solution.maxProfit_kadane(prices)
    print(f"Brute force result: {result_bf}")
    print(f"Kadane's algorithm result: {result_kadane}")
    print(f"All approaches consistent: {result == result_bf == result_kadane}")