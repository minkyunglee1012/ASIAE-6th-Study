import sys
from collections import deque
sys.stdin = open('9093.txt', 'r')
T = int(sys.stdin.readline())
stack = deque()

for i in range(T):
    words = sys.stdin.readline().split()
    for j in words:
        stack.extend(j)
        while stack:
            print(stack.pop(), end='')
        print(end=' ')
    print()