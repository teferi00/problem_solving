"""Solution code for "JUNGOL 3957. Subsequences Summing to Sevens".

- Problem link: https://jungol.co.kr/problem/3957
- Solution link: http://www.teferi.net/ps/problems/jungol/3957
"""

from teflib import io as tio


def main():
    _N, ids = tio.read_int_lines()

    answer = 0
    beg = [-1] + [None] * 6
    cum_sum = 0
    for i, x in enumerate(ids):
        cum_sum = (cum_sum + x) % 7
        if beg[cum_sum] is None:
            beg[cum_sum] = i
        else:
            answer = max(answer, i - beg[cum_sum])

    print(answer)


if __name__ == '__main__':
    main()
