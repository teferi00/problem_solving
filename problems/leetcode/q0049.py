"""Solution code for "LeetCode 49. Group Anagrams".

- Problem link: https://leetcode.com/problems/group-anagrams/
- Solution link: http://www.teferi.net/ps/problems/leetcode/49
"""

import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        for s in strs:
            groups[tuple(collections.Counter(s).items())].append(s)
        return list(groups.values())
