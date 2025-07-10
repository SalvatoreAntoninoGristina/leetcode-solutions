#solution using sliding window

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        r=0
        l=0
        max_len = 0 
        for r in range(len(s)):
            #shift till you find a seen char > 'dvdf'
            while s[r] in seen:
                seen.remove(s[l]) #slide l till windows sees no repetitions
                l += 1
            
            seen.add(s[r]) #try to add r in window
    
            max_len = max(max_len, r - l + 1) #compute max each step 

        return max_len



a = Solution().lengthOfLongestSubstring("abcaaaaaaqwerty")
print(a)