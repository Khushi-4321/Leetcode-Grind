#  leetcode #76: Minimum Window Substring
# Accepted 268 / 268 testcases passed

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t:
            return ""

        # Count characters in t
        t_count = Counter(t)
        required = len(t_count)

        # Sliding window setup
        left, right = 0, 0
        formed = 0
        window_counts = {}
        ans = float("inf"), None, None  # (window length, left, right)

        while right < len(s):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1

            # Check if current char satisfies requirement
            if char in t_count and window_counts[char] == t_count[char]:
                formed += 1

            # Try to shrink window from the left
            while left <= right and formed == required:
                char = s[left]

                # Update answer if smaller window found
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                # Remove leftmost char
                window_counts[char] -= 1
                if char in t_count and window_counts[char] < t_count[char]:
                    formed -= 1

                left += 1

            right += 1

        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]
        