"""Solution code for "Static Range Sum".

- Problem link: https://judge.yosupo.jp/problem/static_range_sum
- Solution link: http://www.teferi.net/ps/problems/yosupo/static_range_sum
"""

from teflib import rangequery
from teflib import io as tio


def main():
    N, Q = tio.read_ints()
    a = tio.read_ints()

    rangesum = rangequery.StaticRangeSum(a)
    for _ in range(Q):
        l, r = tio.read_ints()
        print(rangesum[l:r])


if __name__ == '__main__':
    main()
