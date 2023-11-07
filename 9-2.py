class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        str_list = sorted(list(set(s)))
        print("".join(s for s in str_list))
        return "".join(s for s in str_list)


Solution.removeDuplicateLetters(None, "bcabc")