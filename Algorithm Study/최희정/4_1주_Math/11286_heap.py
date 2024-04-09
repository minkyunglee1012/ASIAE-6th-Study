# https://www.acmicpc.net/problem/11286

# 첫째 줄에 연산의 개수 N(1≤N≤100,000)이 주어진다.
# 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다.
# 만약 x가 0이 아니라면 배열에 x라는 값을 넣는(추가하는) 연산이고,
# x가 0이라면 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다.
# 입력되는 정수는 -231보다 크고, 231보다 작다.

import sys
import heapq


sys.stdin = open("11286.md", "r")
input = sys.stdin.readline

heap = []
T = int(input())

re_val = ''
# heapq.heappush(heap, item) : item을 heap에 추가
# heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 IndexError가 호출됨.
# heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 (in linear time, O(N) )
# heapq.heappop() 의 경우 입력시 (절대값, 본값)을 넣고
# 뽑으면, () 튜플의 첫번째 요소값으로 크기 비교를 하여 가장 작은 값을 추출해 준다.


for i in range(1, T+1):
    in_val = int(input())
    print(f'{i}번째 : {heap}')

    if in_val == 0:
        if heap:
            re_val += str(heapq.heappop(heap)[1]) + '\n'
            print(heapq.heappop(heap)[1])
        else:
            re_val += '0\n'
            # print(0)
    else:
        heapq.heappush(heap, (abs(in_val), in_val))

print(re_val)