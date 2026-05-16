"""Solution code for "LeetCode 128. Longest Consecutive Sequence".

- Problem link: https://leetcode.com/problems/longest-consecutive-sequence
- Solution link: http://www.teferi.net/ps/problems/leetcode/128
"""

import collections
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        return max(
            collections.Counter(
                x - i for i, x in enumerate(sorted(set(nums)))
            ).values(),
            default=0,
        )
