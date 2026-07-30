class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdic ={}

        for n in s:
            if n in sdic:
                sdic[n] += 1
            else:
                sdic[n] =1

        for m in t:
            if m in sdic and sdic[m] != 0:
                sdic[m] -= 1
            else:
                return False

        return True

            

        


