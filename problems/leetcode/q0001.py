"""Solution code for "LeetCode 1. Two Sum".

- Problem link: https://leetcode.com/problems/two-sum/
- Solution link: http://www.teferi.net/ps/problems/leetcode/1
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind_by_num = {}
        for i, x in enumerate(nums):
            if (j := ind_by_num.get(target - x)) is not None:
                return [j, i]
            ind_by_num[x] = i
