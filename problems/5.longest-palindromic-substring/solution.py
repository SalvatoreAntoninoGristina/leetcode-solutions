from typing import Tuple


class Solution:

    def longestPalindrome(self, s: str) -> str:

        i=0
        T=''
        while i in range(len(s)):
            stack = ['-']
            l=i
            r=i

            while l > 0 and s[i] == s[l-1]: l = max (0,l-1)
            while r<len(s)-1 and s[i] == s[r+1]  : r+=1

            center = s[l:r+1]           
        
            if l == 0: l=l
            else: l-=1
            while l >= 0 and  r < len(s)-1 and stack :
                r+=1
                stack.append(s[l])
                if s[r] != stack[-1]: stack = []
                else: 
                    x = stack.pop() 
                    center = x + center + x
                l-=1
               
            if len(T) < len(center): T = center; 

            i+=1
            
        return T


a = Solution().longestPalindrome('xaabacxcabaaxcabaax')
print(a)

