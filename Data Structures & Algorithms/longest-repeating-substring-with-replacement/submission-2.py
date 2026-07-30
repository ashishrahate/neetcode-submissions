class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp ={}
        maxfr = 0
        res = 0
        lstU = 0
        l =0
        for r in range(len(s)):

            mp[s[r]] = 1 + mp.get(s[r], 0)
            maxfr = max(maxfr, mp[s[r]])
            while (r-l+1) - maxfr > k:
                mp[s[r]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res