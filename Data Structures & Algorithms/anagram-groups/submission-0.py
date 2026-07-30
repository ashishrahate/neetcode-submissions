class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False

        countS , countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for m in countS:
            if countS[m] != countT.get(m, 0):
                return False
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        seen =[]
        for i in range(len(strs)):
            if strs[i] not in seen:
                prevLst = [strs[i]]
                for j in range(i+1, len(strs)):
                    if strs[j] not in seen and self.isAnagram(strs[i], strs[j]):
                        seen.append(strs[j])
                        prevLst.append(strs[j])
                res.append(prevLst)
        return res

        