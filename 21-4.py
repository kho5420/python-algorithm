from typing import List


# 134
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start_index = 0
        fuel = 0

        for i in range(len(gas)):
            if gas[i] + fuel < cost[i]:
                start_index = i + 1
                fuel = 0
            else:
                print(gas[i])
                fuel += gas[i] - cost[i]

        return start_index




gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
Solution().canCompleteCircuit(gas, cost)