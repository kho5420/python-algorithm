from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        node = [i for i in range(1, n + 1)]
        total_time_dict = {}

        for time in times:
            #     "start": time[0],
            #     "end": time[1],
            #     "time": time[2],
            total_time_dict[time[0]] = 0 if time[1] == k else time[2]
            node.remove(time[1])

        if node and node[0] != k:
            return -1

        total_time = sum(total_time_dict.values())

        return total_time


# Solution.networkDelayTime(None, [[2,1,1],[2,3,1],[3,4,1]], 4, 2)
# Solution.networkDelayTime(None, [[1, 2, 1], [2, 1, 3]], 2, 2)
Solution.networkDelayTime(None, [[1,2,1],[2,3,2],[1,3,2]], 3, 1)
