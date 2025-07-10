class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        dic = {}
        i=0
        max_=0
        tmp_max=0
            
            
        i = 0
        while i < len(s): #brute force, not optimal
            c = s[i]
            if c not in dic:
                    dic[c]=''
                    tmp_max += 1
                    i+=1
            else:
                 dic = {}
                 max_ = max(max_,tmp_max)
                 i = i-(tmp_max-1)
                 tmp_max = 0
            max_ = max(max_,tmp_max)
        return max_

    
a = Solution().lengthOfLongestSubstring(" ")
print(a)