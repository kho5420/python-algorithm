from typing import List


# 336
class Solution:
    # def palindromePairs(self, words: List[str]) -> List[List[int]]:
    #     result = []
    #
    #     for i, word in enumerate(words):
    #         for j, word2 in enumerate(words):
    #             if word == word2:
    #                 continue
    #
    #             if word + word2 == (word + word2)[::-1]:
    #                 result.append([i, j])
    #
    #     return result

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        result = []

        for i, word in enumerate(words):
            for j, word2 in enumerate(words):
                if word == word2:
                    continue

                if word + word2 == (word + word2)[::-1]:
                    result.append([i, j])

        return result


Solution().palindromePairs(["abcd","dcba","lls","s","sssll"])