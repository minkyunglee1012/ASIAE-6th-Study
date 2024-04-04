# https://www.acmicpc.net/problem/2346
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
balloons = list(enumerate(map(int, input().split())))

move = 0
while T >= 0:
    idx, balloon = balloons.pop(move)
    print(idx+1, end=' ')

    T -= 1
    if T == 0:
        move = 0
        break
    if balloon > 0:
        move = (move + balloon - 1) % T
    elif balloon < 0:
        move = (move + balloon) % T

# 입력
# 10
# 1 -2 3 -4 5 -6 7 -8 9 -10
# 출력
# 1 2 9 3 6 5 7 8 10 4