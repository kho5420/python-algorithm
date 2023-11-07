from typing import List


class Solution:
    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #     day = []
    #
    #     for i in range(0, len(temperatures)):
    #         wait = 0
    #
    #         if i == len(temperatures) - 1:
    #             day.append(0)
    #
    #         for j in range(i + 1, len(temperatures)):
    #             wait = wait + 1
    #
    #             if temperatures[i] < temperatures[j]:
    #                 day.append(wait)
    #                 break
    #             elif j == len(temperatures) - 1:
    #                 day.append(0)
    #             elif temperatures[i] == temperatures[j]:
    #                 continue
    #
    #     print(day)

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        day = []
        temp = [0] * len(temperatures)

        for i in range(0, len(temperatures)):
            for j in range(0, len(day)):
                if day[j] < temperatures[i]:
                    day.pop(j)
                    temp[i - 1] = i - j
                    break
            day.append(temperatures[i])

        print(temp)
        print(len(temp))


# te = [73,74,75,71,69,72,76,73]
te = [34,80,80,80,34,80,80,80,34,34]

Solution.dailyTemperatures(None, te)