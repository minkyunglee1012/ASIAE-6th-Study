class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        ans = []
        for i in range(1, n+1):
            stack.append(i)
            ans.append('Push')
            if i not in target:
                stack.pop()
                ans.append('Pop')
            
            if stack == target:
                break
        
        return ans
