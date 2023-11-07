class Solution:
    def isValid(self, s: str) -> bool:
        stack_list = []
        bracket_dict = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        index = 0

        for bracket in list(s):
            if bracket not in bracket_dict:
                stack_list.append(bracket)
            else:
                if not stack_list or bracket_dict[bracket] != stack_list.pop():
                    return False

        # print(index == 0)
        return index == 0

# Solution.isValid(None, "()[]{}")
# Solution.isValid(None, "{[]}")
Solution.isValid(None, "([)]")
