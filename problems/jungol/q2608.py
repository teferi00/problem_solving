"""Solution code for "JUNGOL 2608. 점 모으기".

- Problem link: https://jungol.co.kr/problem/2608
- Solution link: http://www.teferi.net/ps/problems/jungol/2608
"""

from teflib import io as tio
from teflib.tutorial import min_sum_of_abs


def main():
    N, M = tio.read_ints()
    r, c = tio.read_int_cols(M)

    min_sum_r, _ = min_sum_of_abs.min_sum_of_abs_funcs(r)
    min_sum_c, _ = min_sum_of_abs.min_sum_of_abs_funcs(c)
    answer = min_sum_r + min_sum_c

    print(answer)


if __name__ == '__main__':
    main()
