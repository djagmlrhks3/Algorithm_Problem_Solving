import sys
sys.stdin = open('5204. 병합 정렬.txt', 'r')

# def merge(left, right):
#     global count
#     gather = []
#     while left or right:
#         if left and right:
#             if left[0] > right[0]:
#                 gather.append(right.pop(0))
#             else:
#                 gather.append(left.pop(0))
#         elif left:
#             count += 1
#             gather += left
#             left = []
#         else:
#             gather += right
#             right = []
#     return gather
#
def merge_sort(li):
    global count
    if len(li) == 1: return li
    mid = len(li)//2
    left = li[:mid]
    right = li[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    if left[-1] > right[-1]:count+=1
    return merge(left, right)

def merge(arr1, arr2):
    result = list()
    i = j = 0
    while i < len(arr1) or j < len(arr2):
        if i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
        elif i < len(arr1):
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    return result
T = int(input())
for tc in range(T):
    N = int(input())
    numbers = list(map(int,input().split()))
    count = 0
    print('#{} {} {}'.format(tc+1, merge_sort(numbers)[N//2], count))

"""
#병합정렬
def merge_sort(arr):
    #문제를 절반으로 나누어서 각각을 해결하는 부분
    if len(arr) == 1: return arr
    #절반으로 나누어서 각각의 별도의 정렬 실행
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)
    
def merge(arr1, arr2):
    result = []
    #병합과정 실행
    #각각의 최소값들(가장 앞쪽 값)을 비교해서 더 작은 요소를
    #결과에 추가
    #두 부분집합에 요소가 없어질 때 까지 반복
    while arr1 and arr2:
        #두 부분집합의 요소가 모두 남아있을 경우
        if arr1 and arr2:
            if arr1[0] <= arr2[0]:
                result.append(arr1.pop(0))
            else:
                result.append(arr2.pop(0))
        elif arr1:
            result.append(arr1.pop(0))
        elif arr2:
            result.append(arr2.pop(0))
    return result    
    #두 개의 정렬된 부분집합을 하나의 집합으로 만들어 반환
arr = [5,2,4,1,7,8,9,6,3]

#인덱스 이동하면서 병합하는 함수
def merge2(arr1, arr2):
    result = list()
    i = j = 0
    while i < len(arr1) or j < len(arr2):
        if i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
        elif i < len(arr1):
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    return result
"""
