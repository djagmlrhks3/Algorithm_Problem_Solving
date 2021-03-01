import sys
sys.stdin = open('백준1062. 가르침.txt', 'r')

def dfs(idx, cnt):
    global K, answer
    if cnt == K:
        temp = 0
        for word in words:
            for alpha in word:
                if not check[ord(alpha)-ord('a')]:
                    break
            else:
                temp += 1
        answer = max(answer, temp)
        return

    for i in range(idx, 26):
        if not check[i]:
            check[i] = True
            dfs(i, cnt+1)
            check[i] = False

N, K = map(int, input().split())
if K < 5:
    print(0)
else:
    answer = 0
    K -= 5
    check = [False] * 26
    words = [set(sys.stdin.readline().strip()) for _ in range(N)]
    for alpha in ('a', 'n', 't', 'i', 'c'):
        check[ord(alpha) - ord('a')] = True

    dfs(0, 0)
    print(answer)