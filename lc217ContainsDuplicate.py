# LeetCode #217 - Contains Duplicate
# Accepted: 77/77 | Runtime: 15ms


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) != len(set(nums)):
            return True
        else:
            return False  