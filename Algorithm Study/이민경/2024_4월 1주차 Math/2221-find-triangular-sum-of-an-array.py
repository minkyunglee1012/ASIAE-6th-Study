class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            for i in range(len(nums)):
                if i < len(nums) -1:
                    if nums[i] + nums[i+1] <10:
                        nums[i] = nums[i] + nums[i+1]
                    else:
                        nums[i] = nums[i] + nums[i+1] - 10
                if i == len(nums) -1:
                    nums.pop()

        return nums[0]