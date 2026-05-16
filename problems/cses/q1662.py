"""Solution code for "CSES 1662. Subarray Divisibility".

- Problem link: https://cses.fi/problemset/task/1662
- Solution link: http://www.teferi.net/ps/problems/cses/1662
"""


def main():
    n = int(input())
    a = [int(x) for x in input().split()]

    count_by_cum_sum = [0] * n
    count_by_cum_sum[0] = 1
    cum_sum = 0
    answer = 0
    for x in a:
        cum_sum = (cum_sum + x) % n
        answer += count_by_cum_sum[cum_sum]
        count_by_cum_sum[cum_sum] += 1

    print(answer)


if __name__ == '__main__':
    main()
