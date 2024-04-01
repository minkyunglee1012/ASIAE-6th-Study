class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        couple = {}
        arr = row
        
        # {0:1, 1:0, 2:3, 3:2,,,} 이런식으로 짝별로 딕셔너리에 저장
        for i in range(0, n-1, 2):
            couple[i] = i+1
            couple[i+1] = i
        print(couple)
        swaps = 0

        # n/2 커플 중 (n-1)/2 커플만 보면 됨(순회)
        for i in range(0, n-2, 2):
            if couple[arr[i]] != arr[i+1]:
                print(couple[arr[i]], arr[i+1])
                swaps += 1
                temp = arr.index(couple[arr[i]])
                arr[i+1],arr[temp]  = arr[temp], arr[i+1]



        return swaps