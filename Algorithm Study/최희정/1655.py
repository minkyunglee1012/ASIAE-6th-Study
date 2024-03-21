import sys

sys.stdin = open("1655.md", "r")

T = int(input())
tmp_arr = []
result_val = ''

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tmp = int(input())
    tmp_left = []

    # 삽입하기 전에 크기 비교하기
    if len(tmp_arr) == 0:
        tmp_arr.append(tmp)
    else:
        # for idx, val in enumerate(tmp_arr):
        #     if tmp < val and idx <= len(tmp_arr)-1:
        #         tmp_left = tmp_arr[:idx]
        #         tmp_left.append(tmp)
        #         tmp_left = tmp_left + tmp_arr[idx:]
        #         tmp_arr = tmp_left
        #         break
        #     elif idx == len(tmp_arr)-1:
        #         tmp_arr.append(tmp)
        #         break

        for idx, val in enumerate(tmp_arr):
            if tmp < val and idx <= len(tmp_arr)-1:
                tmp_arr.insert(idx, tmp)
                break
            elif idx == len(tmp_arr)-1:
                tmp_arr.append(tmp)
                break

    # print(tmp_arr)


    if len(tmp_arr) % 2 == 0:
        # 총 배열 짝수개
        mid_val = tmp_arr[len(tmp_arr) // 2 - 1]
    else:
        # 홀수개
        mid_val = tmp_arr[len(tmp_arr) // 2]

    result_val += str(mid_val) + '\n'

print(result_val)
