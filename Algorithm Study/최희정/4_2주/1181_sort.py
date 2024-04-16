# https://www.acmicpc.net/problem/1181

import sys
sys.stdin = open("1181.md", "r")

n = int(input())
dict_val = {}
dict_cnt = {}

max_len = 0
result = ''

for idx in range(n):
    tmp = input()
    if tmp not in dict_val:
        dict_val[tmp] = len(tmp)
        if len(tmp) in dict_cnt:
            dict_cnt[len(tmp)] += [tmp]
        else:
            dict_cnt[len(tmp)] = [tmp]

        if max_len < len(tmp):
            max_len = len(tmp)

dict_size = len(dict_cnt)

for i in range(1, max_len+1):
    # 해당 키값이 존재 하지 않으면 패스
    if i not in dict_cnt:
        continue
    # 해당 문자길의의 단어가 여러개라면
    if len(dict_cnt[i]) > 1:
        voca_list = dict_cnt[i]
        voca_list.sort()
        result += '\n'.join(voca_list) + '\n'
    else:
        result += dict_cnt[i][0] + '\n'

print(result)


