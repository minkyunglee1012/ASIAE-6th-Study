class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        answer = []

        for i in range(len(heights)-1, -1, -1):
            cnt = 0
            # stack[-1]은 heights[i+1]
            while stack and stack[-1] < heights[i]:
                cnt += 1
                stack.pop()
            if stack and stack[-1] > heights[i]:
                cnt += 1
            answer.append(cnt)
            stack.append(heights[i])
            
        return answer[::-1]
    
    
    
# 아래 코드는 타임초과 ㅠㅠ
    
'''heights = [10,6,8,5,11,9]
answer = []
for i in range(len(heights)):
    cnt = 0
    for j in range(i+1, len(heights)):
        # print(min(heights[i], heights[j]))
        # print(heights[i], heights[j])
        if j == i+1 :
            # print(heights[i+1:j+1])
            # print(max(heights[i+1:j+1]))
            cnt += 1
        elif j > i+1 and min(heights[i], heights[j]) >= max(heights[i+1:j]):
            # print(heights[i+1:j])
            # print(max(heights[i+1:j]))
            cnt += 1
    answer.append(cnt)

answer'''

