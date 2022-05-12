import sys
sys.stdin = open('백준18222. 투에-모스 문자열.txt', 'r')
k = int(input())
def recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n%2:
        return 1-recursive(n//2)
    else:
        return recursive(n//2)
print(recursive(k-1))
