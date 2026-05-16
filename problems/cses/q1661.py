"""Solution code for "CSES 1661. Subarray Sums II".

- Problem link: https://cses.fi/problemset/task/1661
- Solution link: http://www.teferi.net/ps/problems/cses/1661
"""

import collections


def main():
    n, x = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]

    counter = collections.Counter([str(0)])
    cum_sum = 0
    answer = 0
    for a_i in a:
        cum_sum += a_i
        answer += counter[str(cum_sum - x)]
        counter[str(cum_sum)] += 1

    print(answer)


if __name__ == '__main__':
    main()
