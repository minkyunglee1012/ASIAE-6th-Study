# https://www.acmicpc.net/problem/10773
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# n = [int(input()) for _ in range(T)] # 이렇게 하면 시간 초과남

stack = []
for _ in range(T):
    num = int(input())
    print(num)
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
print(sum(stack))
