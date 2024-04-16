# https://www.acmicpc.net/problem/1546
import sys

sys.stdin = open("1546.md", "r")
# input = sys.stdin.readline

T = int(input())

# 점수 읽기
inputs = input()
scores = list(map(int, inputs.split(' ')))

# 최대값
max_score = max(scores)
new_scores = []

for idx, score in enumerate(scores):
    score = score/max_score*100
    new_scores.append(score)

# 평균 구하기
print(sum(new_scores)/T)
