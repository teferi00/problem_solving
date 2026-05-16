"""Solution code for "JUNGOL 8259. 최애 연산자".

- Problem link: https://jungol.co.kr/problem/8259
- Solution link: http://www.teferi.net/ps/problems/jungol/8259
"""

from teflib import io as tio
from teflib import rangequery


@tio.run_n_times
def main():
    N, M = tio.read_ints()
    a = tio.read_ints()

    b = sorted(x % M for x in a)
    b += [x + M for x in b]
    sum_b = rangequery.StaticRangeSum(b)
    size = N // 2
    answer = min(
        sum_b[r_beg : r_beg + size] - sum_b[l_beg : l_beg + size]
        for l_beg, r_beg in zip(range(N), range(N - size, N * 2))
    )

    print(answer)


if __name__ == '__main__':
    main()
