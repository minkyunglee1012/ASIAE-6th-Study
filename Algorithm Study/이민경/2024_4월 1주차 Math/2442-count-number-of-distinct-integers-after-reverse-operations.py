class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        result = []

        for i in range(len(nums)):
            result.append(int(str(nums[i])[::-1]))


        return len(set(nums + result))
