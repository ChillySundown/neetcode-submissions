class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()
        left, right = 0, len(s)-1
        while(left <= right):
            left_c = s_lower[left]
            right_c = s_lower[right]

            if not left_c.isalnum():
                left += 1
            elif not right_c.isalnum():
                right -= 1
            else:
                if(right_c != left_c):
                    return False
                else:
                    left += 1
                    right -= 1
        return True
