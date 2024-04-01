class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        
        # 스택에 푸시값을 넣다가 popped[i] 값과 같으면 스택에서 빼준다
        for push in pushed:
            stack.append(push)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1

        return len(stack) == 0
