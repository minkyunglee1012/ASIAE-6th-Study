# https://school.programmers.co.kr/learn/courses/30/lessons/181854

# testcase 1
arr = [49, 12, 100, 276, 33]
n = 27   # [76, 12, 127, 276, 60]

# testcase 2
# arr = [444, 555, 666, 777]
# n = 100   # [444, 655, 666, 877]


def solution(arr, n):
    answer = []
    if len(arr) % 2 == 1:
        for i in range(len(arr)):
            if i % 2 == 0:
                arr[i] = arr[i] + n
        answer = arr
    else:
        for j in range(len(arr)):
            if j % 2 == 1:
                arr[j] = arr[j] + n
        answer = arr
    return answer


print(solution(arr, n))