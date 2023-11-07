from typing import List
from collections import Counter


# 621
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_index = 0
        idle = 0
        n_count = n
        task_dict = dict(Counter(tasks))
        print(task_dict)

        while any(value != 0 for value in task_dict.values()):
            for task in task_dict.keys():
                task_index += 1
                n_count -= 1
                task_dict[task] = task_dict[task] - 1

            if n_count == 0:
                n_count = n

                if any(value != 0 for value in task_dict.values()):
                    idle += 1

        print(task_index)
        print(idle)
        return task_index + idle - 1


    # def leastInterval(self, tasks: List[str], n: int) -> int:
    #     counter = Counter(tasks)
    #     result = 0
    #
    #     while True:
    #         sub_count = 0
    #         # 개수 순 추출
    #         for task, _ in counter.most_common(n + 1):
    #             sub_count += 1
    #             result += 1
    #
    #             counter.subtract(task)
    #             # 0 이하인 아이템을 목록에서 완전히 제거
    #             counter += Counter()
    #
    #         if not counter:
    #             break
    #
    #     result += n - sub_count + 1
    #
    #     return result



tasks = ["A","A","A","B","B","B"]
n = 2
Solution().leastInterval(tasks, n)