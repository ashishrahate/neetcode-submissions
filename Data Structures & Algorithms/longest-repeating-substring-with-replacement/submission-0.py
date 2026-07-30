class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp ={}
        maxfr = 0
        res = 0
        lstU = 0
        l =0
        for r in range(len(s)):
            if s[r] not in mp:
                mp[s[r]] = 1
                lstU = r

            else:
                mp[s[r]] += 1
                maxfr = max(maxfr, mp[s[r]])


            if r-l+1 - maxfr > k:
                l = lstU
            res = max(res, r-l+1)
        return res