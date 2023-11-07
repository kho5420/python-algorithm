from typing import List


# 122
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(0, len(prices)):
            if i == len(prices) - 1:
                break

            if prices[i] < prices[i + 1]:
                result += prices[i + 1] - prices[i]

        print(result)
        return result

# prices = [7,1,5,3,6,4]
prices = [2,1,2,0,1]
Solution().maxProfit(prices=prices)