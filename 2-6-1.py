####
# 2-6 문자열 조작
####
import time

text = ['h', 'e', 'l', 'l', 'o']
text2 = ['H', 'a', 'n', 'n', 'a', 'h']

def reverse_string(str_list):
    # str_list.reverse()

    index = 0
    temp_list = str_list[:]
    for i in range(len(temp_list) - 1, -1, -1):
        str_list[index] = temp_list[i]
        index = index + 1

    print(str_list)

stime = time.time()
reverse_string(text)
reverse_string(text2)
print(f"{time.time() - stime:.10f} sec")