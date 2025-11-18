from collections import Counter
from typing import List

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        
        sign = 1
        index = 0
        if s[0] in ('+', '-'):
            if s[0] == '-':
                sign = -1
            index += 1
        
        result = 0
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            # Check for overflow and underflow
            if result > (2**31 - 1 - digit) // 10:
                return 2**31 - 1 if sign == 1 else -2**31
            result = result * 10 + digit
            index += 1
        
        return sign * result
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)
        s_count = Counter()
        
        result = []
        p_length = len(p)
        
        for i in range(len(s)):
            s_count[s[i]] += 1
            
            if i >= p_length:
                if s_count[s[i - p_length]] == 1:
                    del s_count[s[i - p_length]]
                else:
                    s_count[s[i - p_length]] -= 1
            
            if s_count == p_count:
                result.append(i - p_length + 1)
        
        return result
    
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        return ' '.join(words)