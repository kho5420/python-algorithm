from typing import List


# 393
class Solution:
    def findb(self, bin: str):
        index = bin.find("b")
        return bin[index + 1:]

    def charge(self, string: str):
        print(string)

    def validUtf8(self, data: List[int]) -> bool:
        t1 = self.findb(bin(data[2]))
        t2 = self.charge(t1)
        print(t1)
        print(t2)

        for i, d in enumerate(data):
            if i == 0:
                continue
            else:
                if self.findb(bin(d))[0:2] != "10":
                    return False

        return True

        #
        # if len(data) == 3:
        #     front = self.findb(bin(data[0]))[0:4]
        #     print(front)


d = [197,130,1]
Solution().validUtf8(d)