"""Solution code for "JUNGOL 4005. Hoof, Paper, Scissors".

- Problem link: https://jungol.co.kr/problem/4005
- Solution link: http://www.teferi.net/ps/problems/jungol/4005

[Source] USACO > USACO 2017 January > Silver
"""

from teflib import io as tio
from teflib import rangequery


def main():
    N, gestures = tio.read_str_lines()

    range_sums = {
        x: rangequery.StaticRangeSum([1 if g == x else 0 for g in gestures])
        for x in 'HPS'
    }
    answer = 0
    for i in range(1, N):
        before_change = max(range_sums[g].first_k_sum(i) for g in 'HPS')
        after_change = max(range_sums[g].last_k_sum(N - i) for g in 'HPS')
        answer = max(answer, before_change + after_change)

    print(answer)


if __name__ == '__main__':
    main()
