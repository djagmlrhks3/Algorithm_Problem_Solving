import sys
sys.stdin = open('백준1436. 영화감독 숌.txt', 'r')

N = int(input())
movie = 666

while N:
    if "666" in str(movie):
        N -= 1
    movie += 1

print(movie - 1)