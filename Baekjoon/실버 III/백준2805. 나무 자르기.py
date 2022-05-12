import sys
sys.stdin = open('백준2805. 나무 자르기.txt', 'r')

N, M = map(int, input().split())
trees = list(map(int, sys.stdin.readline().split()))
left, right = 1, max(trees)
while left <= right:
    mid = (left + right) // 2
    get = 0
    for num in trees:
        if num-mid > 0:
            get += (num-mid)

    if get >= M:
        left = mid+1
    else:
        right = mid-1
print(right)