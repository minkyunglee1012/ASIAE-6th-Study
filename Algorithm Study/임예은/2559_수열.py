import sys
sys.stdin = open('2559.txt', 'r')
input = sys.stdin.readline
n, k = map(int, input().split())
a = list(map(int, input().split()))

result = []
result.append(sum(a[:k]))

for i in range(n - k):
    result.append(result[i] - a[i] + a[k + i])

print(max(result))

# 시간 초과
# for i in range(n - k + 1):
#     result.append(sum(a[i:i + k]))