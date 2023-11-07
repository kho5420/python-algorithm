from typing import List

# 179
class Solution:
    def split_digits(self, num):
        if num < 10:
            return num

        digits = []
        while num > 0:
            digit = num % 10
            digits.append(digit)
            num //= 10
        return digits

    def largestNumber(self, nums: List[int]) -> str:
        for i in range(0, len(nums)):
            for j in range(1, len(nums)):
                print()



# nums = [10, 2]
nums_list = [3,30,34,5,9]
Solution().largestNumber(nums_list)
