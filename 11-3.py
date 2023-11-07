class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # length = 0
        # longest_length = 0
        # check = {}
        #
        # for sub in s:
        #     if check.get(sub) is None:
        #         length = length + 1
        #
        #         if length >= longest_length:
        #             longest_length = length
        #     else:
        #         length = 1
        #
        #     check[sub] = 1

        text = ""
        longest_text = ""
        check = {}

        for sub in s:
            if len(text) > 0 and len(text) - 1 == text.find(sub):
                text = sub
                continue

            text = text + sub

            if check.get(sub) is not None:
                text = text.replace(sub, "", 1)

            if len(text) >= len(longest_text):
                longest_text = text

            check[sub] = 1

        return len(longest_text)

Solution.lengthOfLongestSubstring(None, "ckilbkd")