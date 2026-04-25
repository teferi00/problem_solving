"""Solution code for "LeetCode 347. Top K Frequent Elements".

- Problem link: https://leetcode.com/problems/top-k-frequent-elements/
- Solution link: http://www.teferi.net/ps/problems/leetcode/347
"""

import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [key for key, _val in collections.Counter(nums).most_common(k)]
