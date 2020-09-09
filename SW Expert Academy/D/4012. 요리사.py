import sys
sys.stdin = open('4012. 요리사.txt')

def solve(count, index):
    global answer

    if index == n:
        return
    if count == n // 2:
        A, B = 0, 0
        for i in range(n):
            for j in range(n):
                if A_B[i] and A_B[j]:
                    A += taste[i][j]
                if not A_B[i] and not A_B[j]:
                    B += taste[i][j]
        answer = min(answer, abs(A - B))
        return

    A_B[index] = True
    solve(count + 1, index + 1)
    A_B[index] = False
    solve(count, index + 1)


T = int(input())
for tc in range(T):
    n = int(input())
    taste = [list(map(int, input().split())) for _ in range(n)]

    A_B = [False] * n
    answer = 0xfffffff

    solve(0, 0)
    print('#{} {}'.format(tc+1, answer))

