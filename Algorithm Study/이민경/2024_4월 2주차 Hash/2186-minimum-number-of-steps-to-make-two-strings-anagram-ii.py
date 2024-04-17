class Solution:
    def minSteps(self, s: str, t: str) -> int:
        S = {}
        T = {}
        count = 0
        
        for i in s:
            if i in S:
                S[i] += 1
            else:
                S[i] = 1
            
        for i in t:
            if i in T:
                T[i] += 1
            else:
                T[i] = 1
        
        for idx, val in T.items():
            if idx in S:
                if val == S[idx]:
                    S[idx] = 0
                    continue
                else:
                    count += abs(val-S[idx])
                    S[idx] = 0   
            else:
                count += val
        
        
        for val in S.values():
            count += val
        
        return count