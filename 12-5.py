from typing import List


def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    result = []

    def dfs(csum, index, path):
        # 종료 조건
        if csum < 0:
            return
        if csum == 0:
            result.append(path)
            return

        # 자신 부터 하위 원소까지의 나열 재귀 호출
        for i in range(index, len(candidates)):
            dfs(csum - candidates[i], i, path + [candidates[i]])

    dfs(target, 0, [])
    return result

combinationSum(None, [2,3,6,7], 7)