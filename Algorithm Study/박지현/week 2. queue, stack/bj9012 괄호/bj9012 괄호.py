# https://www.acmicpc.net/problem/9012

import sys
sys.stdin = open("input.txt", "r")
T = int(input())
test_cases = [list(map(str, input())) for _ in range(T)]
print(test_cases)

for a in test_cases:
    print(a)
    FLAG = True
    stack = []
    for char in a:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                print('NO')
                FLAG = False
                break
            stack.pop()
    if not FLAG:
        continue
    if stack:
        print('NO')
    else:
        print('YES')
