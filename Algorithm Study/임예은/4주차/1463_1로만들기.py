import sys
sys.stdin = open('1463.txt', 'r')
input = sys.stdin.readline
n = int(input())

dp = [0] * 1000001

# dp[i]는 i를 1로 만들기 위해 필요한 최소 횟수
for i in range(2, n+1):
    # 현재의 수에서 1을 빼는 경우
    dp[i] = dp[i-1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

# 결과 출력
print(dp[n])