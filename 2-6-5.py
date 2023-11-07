####
# 2-6 문자열 조작
####
import re
import time

palindromic = "babad"
palindromic2 = "cbbd"

def is_palindromic(text):
    text = text.lower()
    text = re.sub('[^a-zA-Z0-9]', ' ', text).replace(" ", "")

    result = True
    for i in range(0, len(text)):
        if text[i] == text[len(text) - i - 1]:
            continue
        else:
            result = False
            break

    return result

def find_longest_palindromic(word):
    print(word)
    result = ""

    for i in range(0, len(word)):
        if len(word[i:]) > 1 and is_palindromic(word[i:]):
            result = word[i:]
            break
        elif len(word[:i]) > 1 and is_palindromic(word[:i]):
            result = word[:i]
            break
        elif len(word[i:len(word) - i]) > 1 and is_palindromic(word[i:len(word) - i]):
            result = word[i:len(word) - i]
            break

    print(f"result : {result}")

stime = time.time()
find_longest_palindromic(palindromic)
print("==================================")
find_longest_palindromic(palindromic2)
print(f"{time.time() - stime:.10f} sec")