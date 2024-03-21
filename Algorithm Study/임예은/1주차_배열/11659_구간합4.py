import sys
sys.stdin = open('11659.txt', 'r')
input = sys.stdin.readline

m, n = map(int, input().split())
arr = list(map(int, input().split()))
prefix_sum = [0]
temp = 0

# 누적합 저장
for i in arr:
    temp += i
    prefix_sum.append(temp)

# i~j까지 합 구하기
for i in range(n):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a - 1])