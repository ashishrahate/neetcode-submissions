class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdic ={}
        tdic={}

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

            

        


