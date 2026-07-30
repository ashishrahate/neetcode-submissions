class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = [c.lower() for c in s if c.isalnum()]
        return check == check[::-1]

        # l, r = 0, len(s)-1
        # l_lower , r_lower = '', ''
        # while l <= r:
        #     if s[l].isalnum():
        #         l_lower = s[l].lower()
        #     else:
        #         l += 1
        #         continue
            
        #     if s[r].isalnum():
        #         r_lower = s[r].lower()
        #     else:
        #         r -= 1
        #         continue

        #     if l_lower != r_lower :
        #         return False
        #     else:
        #         r -= 1
        #         l += 1

        # return True
            


        