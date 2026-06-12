class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        max_len = 0
        i = 0
        n = len(s)
        
        while i < n:
            zeros = 0
            ones = 0
            
            # Count consecutive zeros
            while i < n and s[i] == '0':
                zeros += 1
                i += 1
                
            # Count consecutive ones
            while i < n and s[i] == '1':
                ones += 1
                i += 1
                
            # The valid balanced length is 2 * min(zeros, ones)
            max_len = max(max_len, 2 * min(zeros, ones))
            
        return max_len