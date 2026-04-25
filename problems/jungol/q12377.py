"""Solution code for "JUNGOL 12377. 인형 뽑기".

- Problem link: https://jungol.co.kr/problem/12377
- Solution link: http://www.teferi.net/ps/problems/jungol/12377
"""


def main():
    N, A1, A2, B, C1, C2 = [int(x) for x in input().split()]

    answer = max(0, (N - B)) // C1 * C2
    if A1 <= N:
        answer = max(answer, A2 + max(0, (N - A1 - B)) // C1 * C2)

    print(answer)


if __name__ == "__main__":
    main()
