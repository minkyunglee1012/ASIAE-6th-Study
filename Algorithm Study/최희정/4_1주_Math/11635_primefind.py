# https://www.acmicpc.net/problem/11653
import sys

sys.stdin = open("11635.md", "r")
N = int(input())

# 소인수 분해 하기
def prime_find(num):
    if num <= 2:
        return [num,]
    for i in range(2, num):
        if num % i == 0:
            # temp_list = []
            val_x = prime_find(i)
            val_y = prime_find(int(num/i))
            temp_list = val_x + val_y
            return temp_list
    return [num,]

def solution():
    if N == 1:
        return

    prime_num_list = prime_find(N)

    result = ''
    for re_val in prime_num_list:
        result += str(re_val) + '\n'

    print(result)
    return


solution()
