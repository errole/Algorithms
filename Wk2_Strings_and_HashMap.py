class Solution:
    def reverseWords(self, s: str) -> str:

        s = s.strip().split()
        start = 0
        end = len(s)-1

        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

        return ' '.join(s)
    
    def myAtoi(self, s: str) -> int:
        pattern = r'^\s*([\+\-]?)0*([1-9][0-9]*)'
        match = re.search(pattern, s)
        if match:
            r_value = int(match.group(1) + match.group(2))
            if r_value < -2**31:
                r_value = -2**31
            elif r_value > 2**31 -1:
                r_value = 2**31 -1
            return r_value
        else:
            return 0
        
    def findAnagrams(s: str, p: str) -> list[int]:
        res = []
        p_len = len(p)
        s_len = len(s)
            
        if p_len > s_len:
            return res
        
        p_count = Counter(p)
        window_count = Counter(s[:p_len - 1])

        for i in range(p_len - 1, s_len):
            window_count[s[i]] += 1
            start = i - p_len + 1
            if window_count == p_count:
                res.append(start)
            window_count[s[start]] -= 1
            if window_count[s[start]] == 0:
                del window_count[s[start]]

        return res


if __name__ == "__main__":
    s = "the sky is blue"
    print(Solution().reverseWords(s))

