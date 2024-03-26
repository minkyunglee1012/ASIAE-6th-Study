import sys
sys.stdin = open('1406.txt', 'r')
input = sys.stdin.readline

str = list(input().strip())
temp = []
m = int(input())
for _ in range(m):
    command = input().split()
    if command[0] == 'L':
        if str:
            temp.append(str.pop())
    elif command[0] == 'D':
        if temp:
            str.append(temp.pop())
    elif command[0] == 'B':
        if str:
            str.pop()
    elif command[0] == 'P':
        str.append(command[1])
print(''.join(str + list(reversed(temp))))