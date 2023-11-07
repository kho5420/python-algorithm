####
# 2-6 문자열 조작
####
import time

logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]

def sort_logs(log_list):
    first_list = []
    second_list = []

    for log in log_list:
        if log.split()[1].isdigit():
            second_list.append(log)
        else:
            first_list.append(log)

    print(first_list)
    print(second_list)

    first_list = sorted(first_list, key=lambda x: x[0])
    print(first_list)
    print(first_list + second_list)

stime = time.time()
sort_logs(logs)
print(f"{time.time() - stime:.10f} sec")