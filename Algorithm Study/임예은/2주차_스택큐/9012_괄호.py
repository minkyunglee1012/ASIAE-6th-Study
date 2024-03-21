import sys
from collections import deque
sys.stdin = open('9012.txt', 'r')
T = int(sys.stdin.readline())

for i in range(T):
    stack = deque()
    str = sys.stdin.readline()
    for ch in str:
        if ch == '(':
            stack.append(ch)
        elif ch ==')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    # for else 구문: for문 끝까지 돌았을 경우 실행
    else:
        if stack:
            print('NO')
        else:
            print('YES')