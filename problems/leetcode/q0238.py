"""Solution code for "LeetCode 238. Product of Array Except Self".

- Problem link: https://leetcode.com/problems/product-of-array-except-self/
- Solution link: http://www.teferi.net/ps/problems/leetcode/238
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref_prods = [x := 1] + [x := x * num for num in nums]
        suff_prods = [x := 1] + [x := num * x for num in reversed(nums)]
        n = len(nums)
        return [pref_prods[i] * suff_prods[n - i - 1] for i in range(n)]

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [x := 1] + [x := x * num for num in nums]
        suffix_prod = [x := 1] + [x := num * x for num in reversed(nums)]
        n = len(nums)
        return [prefix_prod[i] * suffix_prod[n - i - 1] for i in range(n)]
