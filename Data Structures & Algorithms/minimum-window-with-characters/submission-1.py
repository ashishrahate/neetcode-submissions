class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '': return ''

        window, countT = {}, {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        res, reslen = [-1, -1], float('inf')
        have, need = 0, len(countT)
        l =0

        for r in range(len(s)):
            c = s[r]
            

            if c in t:
                window[c] = 1 + window.get(c, 0)
                if window[c] == countT[c]:
                    have += 1

            while have == need:
                if (r-l+1)< reslen:
                    res = l, r
                    reslen = r-l+1

                 #will this throw an error?
                if s[l] in t:
                    window[s[l]] -= 1
                    if window[s[l]] < countT[s[l]]:
                        have -= 1

                l += 1
        l, r = res
        return s[l:r+1] if reslen != float('inf') else ''

