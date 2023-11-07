# Definition for singly-linked list.
from typing import Optional, List


# 56
class Solution:
    # def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    #     new_list = []
    #     for num in intervals:
    #         new_list.append(list(range(num[0], num[1] + 1)))
    #
    #     result = []
    #     remove = []
    #     for i, num in enumerate(new_list):
    #         if i == len(new_list) - 1:
    #             break
    #         else:
    #             if set(new_list[i]) & set(new_list[i + 1]):
    #                 print(f"set : {new_list[i], new_list[i+1]}")
    #                 print(new_list[i] + new_list[i+1])
    #                 temp = new_list[i] + new_list[i+1]
    #                 result.append([min(temp), max(temp)])
    #                 remove = remove + intervals[i] + intervals[i+1]
    #
    #     print(remove)
    #     for num in intervals:
    #         if set(num) & set(remove):
    #             print("remove")
    #         else:
    #             result.append(num)
    #     print(result)
    #     return result

    # def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    #     if len(intervals) == 1:
    #         return intervals
    #
    #     new_list = []
    #     for num in intervals:
    #         new_list.append(list(range(num[0], num[1] + 1)))
    #
    #     result = []
    #
    #     origin_length = len(intervals)
    #
    #     i = 0
    #     for num in new_list:
    #         if i == len(new_list) - 1:
    #             break
    #         else:
    #             if set(new_list[i]) & set(new_list[i + 1]):
    #                 temp = new_list[i] + new_list[i+1]
    #                 new_list[i+1] = [min(temp), max(temp)]
    #
    #                 del new_list[i]
    #                 i = i - 1
    #
    #                 if result:
    #                     result.append([min(temp), max(temp)])
    #                     result = self.merge(result)
    #                 else:
    #                     result.append([min(temp), max(temp)])
    #             else:
    #                 if origin_length == 2:
    #                     return intervals
    #
    #                 result.append([min(new_list[i+1]), max(new_list[i+1])])
    #
    #         i = i + 1
    #
    #     print(result)
    #     return result

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        for i in sorted(intervals, key=lambda x: x[0]):
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged += i,
        return merged


Solution().merge([[1,3],[2,6],[8,10],[15,18]])
# Solution().merge([[1,4],[0,2],[3,5]])
# Solution().merge([[1,4],[5,6]])
