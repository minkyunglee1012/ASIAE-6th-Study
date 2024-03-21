import sys
sys.stdin = open('1874.txt', 'r')

for i in range(2):
    n = int(sys.stdin.readline())
    stack = []
    op = []
    count = 1
    for j in range(n):
        num = int(sys.stdin.readline())
        while count <= num:
            stack.append(count)
            op.append('+')
            count += 1
        if stack[-1] == num:
            stack.pop()
            op.append('-')
        elif count > num:
            print('NO')
            break
    else:
        for k in op:
            print(k)