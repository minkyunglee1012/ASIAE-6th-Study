# https://www.acmicpc.net/problem/10845
# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys
from collections import deque
sys.stdin = open("10845.md", "r")

T = int(input())

deq = deque()
re_val = ''
re_err = '-1\n'

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    in_val = input().split()

    # push 3
    if in_val[0] == 'push':
        deq.append(in_val[1])
    # 맨 왼쪽 1개 pop
    elif in_val[0] == 'pop':
        if deq:
            re_val += str(deq.popleft()) + '\n'
        else:
            re_val += re_err
    # 맨 앞의 값 출력
    elif in_val[0] == 'front':
        if deq:
            re_val += str(deq[0]) + '\n'
        else:
            re_val += re_err
    # 맨 뒤의 값 출력
    elif in_val[0] == 'back':
        if deq:
            re_val += str(deq[len(deq)-1]) + '\n'
        else:
            re_val += re_err
    # deq 사이즈
    elif in_val[0] == 'size':
        re_val += str(len(deq)) + '\n'
    # 비었는가
    elif in_val[0] == 'empty':
        if deq:
            re_val += '0\n'
        else:
            re_val += '1\n'

print(re_val)