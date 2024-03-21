# 2428. Maximum Sum of an Hourglass
class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        hourglass = []

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i+2 <= len(grid)-1 and j+2 <= len(grid[0]) -1:
                    hourglass.append(sum(grid[i][j:j+3]) + grid[i+1][j+1] + sum(grid[i+2][j:j+3]))

        return max(hourglass)


# 1314. Matrix Block Sum
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        result = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                result[i][j] = sum(sum(mat[x][max(0, j-k):min(n, j+k+1)])
                                   for x in range(max(0, i-k), min(m, i+k+1)))
        return result



# 238. Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) == 1:
            mul = 1
            for i in range(len(nums)):
                if nums[i] != 0:
                    mul *= nums[i]

            answer = [0]*len(nums)
            answer[nums.index(0)] = mul
            
            return answer

        elif nums.count(0) >= 2:
            answer = [0] * len(nums)
            
            return answer

        else:
            answer = []
            mul = 1
            for i in range(len(nums)):
                mul *= nums[i]

            for i in range(len(nums)):
                answer.append(int(mul / nums[i]))


        return answer
