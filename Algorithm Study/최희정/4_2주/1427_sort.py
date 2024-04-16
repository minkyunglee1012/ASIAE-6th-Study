# https://www.acmicpc.net/problem/1427

import sys
sys.stdin = open("1427.md", "r")

# input_val = '500613009'
input_val = input()
size = len(input_val)
re_val = [0] * size

tmp = [0, 0]

for i in range(size):
    flag = False
    val = int(input_val[i])

    for j in range(i):
        tmp = int(re_val[j])

        # 새로 읽은 숫자가 이전에 자리한 숫자보다 더 크다면
        # 자리 바꾸기
        if val > tmp:
            re_val[j+1:i+1] = re_val[j:i]
            re_val[j] = val
            flag = True
            break
        else:
            continue

    if flag == False:
        re_val[i] = val

sort_val = ''.join(str(s) for s in re_val)
print(sort_val)