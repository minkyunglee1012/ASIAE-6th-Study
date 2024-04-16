# https://leetcode.com/problems/count-sorted-vowel-strings/description/

# Input:
n = 33
# Output: 15
# Explanation: The 15 sorted strings that consist of vowels only are
# ["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
# Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.

vowel = ['a', 'e', 'i', 'o', 'u']

def repeat_vowel(arr, n):

    result = []
    arr_len = len(arr)

    # 끝내는 시기 설정
    if n == 1:
        return arr

    for i in range(arr_len):
        val = arr[i]

        # 재귀를 이용하기 위하여
        # 다음단계 배열을 재조합한다.
        # 이전 단어는 조합하지 않기위해 i부터 시작함.
        new_arr = arr[i:]

        # new_arr로 다시 수행, n-1개 요소
        res_list = repeat_vowel(new_arr, n-1)

        for iter_val in res_list:
            result.append(val + iter_val)

    return result

re_val = repeat_vowel(vowel, n)

print(len(re_val))
