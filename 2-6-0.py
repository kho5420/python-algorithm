####
# 2-6 문자열 조작
####
import re
import time

palindromic_text = "A man, a plan, a canal: Panama"
palindromic_text2 = "race a car"

def is_palindromic(text):
    text = text.lower()
    text = re.sub('[^a-zA-Z0-9]', ' ', text).replace(" ", "")

    result = True
    print(len(text))
    print("======================")
    for i in range(0, len(text)):
        print(len(text) - i)
        if text[i] == text[len(text) - i - 1]:
            continue
        else:
            result = False
            break

    print(result)

stime = time.time()
is_palindromic(palindromic_text)
is_palindromic(palindromic_text2)
print(f"{time.time() - stime:.10f} sec")