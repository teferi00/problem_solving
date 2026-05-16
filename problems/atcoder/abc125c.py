"""Solution code for "AtCoder ABC125-C. GCD on Blackboard".

- Problem link: https://atcoder.jp/contests/abc125/tasks/abc125_c
- Solution link: http://www.teferi.net/ps/problems/atcoder/abc125c
"""

import math


def reduce_except_one(func, seq):
    n = len(seq)
    p, s = seq[0], seq[-1]
    pref = [None, p] + [p := func(p, seq[i]) for i in range(1, n)]
    suff = [None, s] + [s := func(seq[i], s) for i in range(n - 2, -1, -1)]
    return [
        suff[-2],
        *(func(pref[i], suff[n - i - 1]) for i in range(1, n - 1)),
        pref[-2],
    ]


def main():
    _N = int(input())
    A = [int(x) for x in input().split()]
    print(max(reduce_except_one(math.gcd, A)))


if __name__ == '__main__':
    main()
