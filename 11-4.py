class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}

        for num in nums:
            if freq.get(num) is not None:
                freq[num] = freq[num] + 1
            else:
                freq[num] = 1

        top_freq_list = []

        freq = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}

        for key in freq.keys():
            top_freq_list.append(key)

            if len(top_freq_list) == k:
                break

        return top_freq_list


Solution.topKFrequent(None, [1, 1, 1, 2, 2, 3], 2)