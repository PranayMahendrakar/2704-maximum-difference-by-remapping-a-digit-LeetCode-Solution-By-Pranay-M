class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        
        # For maximum: replace first non-9 digit with 9
        max_val = num
        for c in s:
            if c != '9':
                max_val = int(s.replace(c, '9'))
                break
        
        # For minimum: replace first digit with 0
        min_val = int(s.replace(s[0], '0'))
        
        return max_val - min_val