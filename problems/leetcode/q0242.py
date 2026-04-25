"""Solution code for "LeetCode 242. Valid Anagram".

- Problem link: https://leetcode.com/problems/valid-anagram/
- Solution link: http://www.teferi.net/ps/problems/leetcode/242
"""

import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)
