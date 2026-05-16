"""Solution code for "AtCoder ABC164-D. Multiple of 2019".

- Problem link: https://atcoder.jp/contests/abc164/tasks/abc164_d
- Solution link: http://www.teferi.net/ps/problems/atcoder/abc164d
"""

import collections


def main():
    S = input()

    suff_nums = [0]
    p = 1
    for c in reversed(S):
        suff_nums.append((suff_nums[-1] + int(c) * p) % 2019)
        p = p * 10 % 2019
    answer = sum(
        x * (x - 1) // 2 for x in collections.Counter(suff_nums).values()
    )

    print(answer)


if __name__ == '__main__':
    main()
