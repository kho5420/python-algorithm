####
# 2-6 문자열 조작
####
import time

anagrams = ["eat", "tea", "tan", "ate", "nat", "bat"]

def find_anagram(word_list):
    temp_dict = {}
    anagram_list = []

    for i in range(0, len(word_list)):
        temp = "".join(sorted(word_list[i]))
        if temp_dict.get(f"{temp}"):
            temp_dict[f"{temp}"].append(word_list[i])
        else:
            temp_dict[f"{temp}"] = [word_list[i]]

    for key in temp_dict.keys():
        anagram_list.append(temp_dict.get(key))

    print(anagram_list)

stime = time.time()
find_anagram(anagrams)
print(f"{time.time() - stime:.10f} sec")