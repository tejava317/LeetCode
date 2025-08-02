class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        substring = set()
        ans = 0

        while right < len(s):
            if not s[right] in substring:
                substring.add(s[right])
                ans = max(ans, len(substring))
            else:
                while s[right] in substring:
                    substring.remove(s[left])
                    left += 1
                substring.add(s[right])
            right += 1
        
        return ans