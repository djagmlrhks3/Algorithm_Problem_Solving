import sys
sys.stdin = open('백준20057. 마법사 상어와 토네이도.txt', 'r')

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
print(matrix)