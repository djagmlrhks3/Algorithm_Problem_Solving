import sys
sys.stdin = open('백준1920. 수 찾기.txt', 'r')

def find(num):
    left, right = 0, N-1
    if A[left] == num or A[right] == num:
        return 1
    while left < right:
        mid = (left + right) // 2
        if A[mid] > num:
            right = mid-1
        elif A[mid] < num:
            left = mid+1
        else:
            return 1
    return 0

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
A.sort()
M = int(input())
T = list(map(int, sys.stdin.readline().split()))
for num in T:
    print(find(num))