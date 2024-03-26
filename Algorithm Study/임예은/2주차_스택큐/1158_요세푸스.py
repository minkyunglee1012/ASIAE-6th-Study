import sys
from collections import deque
sys.stdin = open('1158.txt', 'r')
input = sys.stdin.readline

n, k = map(int, input().split())
queue = deque(range(1, n+1))
progression = []

while queue:
    for _ in range(k-1):
        queue.append(queue.popleft())
    progression.append(queue.popleft())
print(str(progression).replace('[', '<').replace(']', '>'))