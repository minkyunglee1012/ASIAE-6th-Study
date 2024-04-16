import sys
sys.stdin = open("1302.md", "r")

n = int(input())
dict_val = {}

for idx in range(n):
    tmp = input()

    if tmp in dict_val.keys():
        dict_val[tmp] += 1
    else:
        dict_val[tmp] = 1

# 리스트 컴프리헨션 이용 --- 최대 횟수를 가진 단어 찾기
tmp = [k for k,v in dict_val.items() if max(dict_val.values()) == v]

# 결과 단어가 여러개 인 경우 오름차순으로 소팅
tmp.sort()
print(tmp[0])