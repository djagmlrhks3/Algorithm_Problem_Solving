import sys
sys.stdin = open('1219. 길찾기.txt', 'r')

def dfs(num):
    global res
    if num == '99':
        res = 1; return
    if matrix.get(num):
        for start in matrix.get(num):
            dfs(start)
    else: return
for tc in range(10):
    T, N = map(int, input().split())
    matrix = dict()
    res = 0
    visited = []
    input_num = input().split()
    for i in range(0, len(input_num), 2):
        if input_num[i] not in list(matrix.keys()):
            matrix[input_num[i]] = [input_num[i+1]]
        else:
            matrix[input_num[i]].append(input_num[i+1])
    for start in matrix.get('0'):
        dfs(start)
    print('#{} {}'.format(tc+1, res))