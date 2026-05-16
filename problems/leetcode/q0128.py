"""Solution code for "LeetCode 128. Longest Consecutive Sequence".

- Problem link: https://leetcode.com/problems/longest-consecutive-sequence
- Solution link: http://www.teferi.net/ps/problems/leetcode/128
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        inf = max(nums) + 2
        num_set = set(nums)
        answer = 0
        for x in num_set:
            if x - 1 in num_set:
                continue
            length = next(i for i in range(x, inf) if i not in num_set) - x
            answer = max(answer, length)
        return answer
