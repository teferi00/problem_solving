"""Solution code for "JUNGOL 4002. Hoof, Paper, Scissors".

- Problem link: https://jungol.co.kr/problem/4002
- Solution link: http://www.teferi.net/ps/problems/jungol/4002

[Source] USACO > USACO 2017 January > Gold
"""

from teflib import io as tio


def main():
    N, K = tio.read_ints()
    gestures = tio.read_str_lines(N)

    dp_cur = [{'H': 0, 'P': 0, 'S': 0} for _ in range(K + 1)]
    for g_i in gestures:
        dp_cur, dp_prev = [{} for _ in range(K + 1)], dp_cur
        for k in range(K + 1):
            max_prev = 0 if k == 0 else max(dp_prev[k - 1].values())
            for g in 'HPS':
                dp_cur[k][g] = max(max_prev, dp_prev[k][g])
            dp_cur[k][g_i] += 1

    answer = max(max(dp_cur[k].values()) for k in range(K + 1))
    print(answer)


if __name__ == '__main__':
    main()
