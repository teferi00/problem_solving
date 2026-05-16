"""Solution code for "CSES 1646. Static Range Sum Queries".

- Problem link: https://cses.fi/problemset/task/1646
- Solution link: http://www.teferi.net/ps/problems/cses/1646
"""

from teflib import rangequery
from teflib import io as tio


def main():
    n, q = tio.read_ints()
    x = tio.read_ints()
    sum_x = rangequery.StaticRangeSum(x)
    for a, b in tio.read_ind_mat(q):
        print(sum_x[a : b + 1])


if __name__ == '__main__':
    main()
