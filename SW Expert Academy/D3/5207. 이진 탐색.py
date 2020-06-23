import sys
sys.stdin = open('5207. 이진 탐색.txt', 'r')

def BS(low, high, m, direction):
    global result
    if low > high:return
    else:
        mid = (low + high) // 2
        if m == N[mid]:
            result += 1
            return
        elif m < N[mid]:
            if direction == 'L':return
            BS(low, mid-1, m, 'L')
        else:
            if direction == 'R':return
            BS(mid+1, high, m, 'R')

# def binarysearch(n, m):
#     global result
#     direction = ''
#     low = 0
#     high = n
#     while low <= high:
#         mid = low + (high - low) // 2
#         if N[mid] == m:
#             result += 1
#             return
#         elif N[mid] > m:
#             if direction == 'L':
#                 break
#             high = mid - 1
#             direction = 'L'
#         else:
#             if direction == 'R':
#                 break
#             low = mid + 1
#             direction = 'R'

T = int(input())
for tc in range(T):
    N, M = map(int,input().split())
    N = list(map(int,input().split()))
    N.sort()
    M = list(map(int,input().split()))
    result = 0
    for m in M:
        BS(0, len(N)-1, m, '')
        # binarysearch(len(N)-1,m)
    print('#{} {}'.format(tc+1, result))