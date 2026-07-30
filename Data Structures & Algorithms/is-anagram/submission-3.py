class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdic ={}
        tdic={}
        if len(s) != len(t): return False
        for n in s:
            if n in sdic:
                sdic[n] += 1
            else:
                sdic[n] = 1

        for m in t:
            if m not in sdic or sdic[m] < 0:
                return False
            else:
                sdic[m] -= 1

        return True  

        # if len(s)!= len(t):
        #     return False

        # countS , countT = {}, {}
        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i], 0)
        #     countT[t[i]] = 1 + countT.get(t[i], 0)
        # for m in countS:
        #     if countS[m] != countT.get(m, 0):
        #         return False
        # return True

        


