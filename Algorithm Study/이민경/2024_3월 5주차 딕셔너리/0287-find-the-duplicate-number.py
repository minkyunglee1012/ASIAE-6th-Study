class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}

        for idx, val in enumerate(nums):
            if val not in d:
                d[val] = []
            d[val].append(idx)

        for i, v in d.items():
            if len(v) > 1:
                # print(i)
                return i