class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        i, j = 0, 0
        current = 0
        seen_set = set()
        while(j < len(s) and i <= j):
            if s[j] not in seen_set:
                seen_set.add(s[j])
                j += 1
                current += 1
            else:
                while i < j and s[j] in seen_set:
                    seen_set.remove(s[i])
                    i += 1
                    current -= 1
            if current > max_count:
                max_count = current

        return max_count
            
