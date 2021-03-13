import sys
sys.stdin = open('백준1992. 쿼드트리.txt', 'r')

def check(i, j, size):
    global maps, answer
    compare = maps[i][j]
    for r in range(i, i+size):
        for c in range(j, j+size):
            if maps[r][c] != compare:
                answer += '('
                return False

    for r in range(i, i + size):
        for c in range(j, j + size):
            maps[r][c] = '2'
    if compare == '1':
        answer += '1'
    else:
        answer += '0'
    return True

def recursive(r, c, size):
    global answer
    if size == 1 and maps[r][c] != '2':
        if maps[r][c] == '0':
            answer += '0'
        elif maps[r][c] == '1':
            answer += '1'
        maps[r][c] = '2'
        return
    if not check(r, c, size):
        recursive(r, c, size // 2)
        recursive(r, c + size//2, size//2)
        recursive(r + size // 2, c, size // 2)
        recursive(r + size // 2, c + size // 2, size // 2)
        answer += ')'

N = int(input())
maps = [list(' '.join(sys.stdin.readline().split())) for _ in range(N)]
answer = ''
recursive(0, 0, N)
print(answer)