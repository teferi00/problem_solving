"""Solution code for "LeetCode 217. Contains Duplicate".

- Problem link: https://leetcode.com/problems/contains-duplicate/
- Solution link: http://www.teferi.net/ps/problems/leetcode/217
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
