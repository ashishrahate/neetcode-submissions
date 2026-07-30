class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizestr=''
        chrstr=''
        res= ''
        for i in strs:
            sizestr += str(len(i))+','
            chrstr += i
        print(sizestr)
        print(chrstr)
        sizestr += '#'
        res = sizestr + chrstr
        return res

        



    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, res, i = [], [], 0
        while s[i] != '#':
            cur = ""
            while s[i] != ',':
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1
        i += 1
        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        return res
