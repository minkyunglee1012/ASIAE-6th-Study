class Solution:
    def minSteps(self, s: str, t: str) -> int:
        hashS = {}
        hashT = {}
        cnt = 0

        for i in s:
            if i in hashS:
                hashS[i] += 1
            else:
                hashS[i] =1

        for i in t:
            if i in hashT:
                hashT[i] += 1
            else:
                hashT[i] = 1

        print(hashS, hashT, sep='\n')

        for idx, val in hashT.items():
            # print(idx, val)
            if idx not in hashS:
                print(idx)
                cnt += val
                hashT[idx] = 0

            else:
                if val > hashS[idx]:
                    # print(idx)
                    cnt += val-hashS[idx]

        return cnt