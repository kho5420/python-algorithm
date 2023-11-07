####
# 2-6 문자열 조작
####
import time
from collections import Counter

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

def find_word(words, ban_list):
    words = words.lower()
    ban_list.append(".")
    ban_list.append(",")

    for ban in ban_list:
        words = "".join(words.split(ban))

    words = "".join(words).split()
    print(Counter(words).most_common()[0][0])


stime = time.time()
find_word(paragraph, banned)
print(f"{time.time() - stime:.10f} sec")