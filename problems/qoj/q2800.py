"""Solution code for "QOJ 2800. Monument Tour".

- Problem link: https://qoj.ac/problem/2800
- Solution link: http://www.teferi.net/ps/problems/qoj/2800

[Source] ICPC > SWERC 2018
"""

import collections
from teflib import io as tio
from teflib.tutorial import min_sum_of_abs


def main():
    X, Y = tio.read_ints()
    N = tio.read_int()

    y_coords_by_x = collections.defaultdict(set)
    for _ in range(N):
        x, y = tio.read_ints()
        y_coords_by_x[x].add(y)

    target_y_coords = []
    for y_coords in y_coords_by_x.values():
        if len(y_coords) == 1:
            target_y_coords.append(y_coords.pop())
        else:
            target_y_coords.append(max(y_coords))
            target_y_coords.append(min(y_coords))

    min_y_dist, _ = min_sum_of_abs.min_sum_of_abs_funcs_v0(target_y_coords)
    answer = min_y_dist * 2 + X - 1

    print(answer)


if __name__ == '__main__':
    main()
