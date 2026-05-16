"""Solution code for "CSES 1662. Subarray Divisibility".

- Problem link: https://cses.fi/problemset/task/1662
- Solution link: http://www.teferi.net/ps/problems/cses/1662
"""

from teflib.labs import intset


def main():
    n = int(input())
    a = [int(x) for x in input().split()]

    pref_sums = [x := 0] + [x := (x + a_i) % n for a_i in a]
    answer = sum(
        count * (count - 1) // 2
        for count in intset.FrozenIntCounter(pref_sums).values()
    )

    print(answer)


if __name__ == '__main__':
    main()
