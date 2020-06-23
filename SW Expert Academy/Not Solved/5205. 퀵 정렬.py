import sys
sys.stdin = open('5205. 퀵 정렬.txt', 'r')

def quick_sort(arr, left, right): #왼쪽 시작점, 오른쪽 끝지점을 알아야 함!
    # pivot의 위치를 결정한다.(피봇을 기준으로 큰값은 오른쪽, 작은 값은 왼쪽으로 구분)
    # 왼쪽 부분집합 정렬
    # 오른쪽 부분집합 정렬
    if left > right:
        # 피봇 구하기
        pivot = lomuto_partition(arr, left, right)
        # 왼쪽 부분집합 정렬 실행
        quick_sort(arr, left, pivot-1)
        # 오른쪽 부분집합 정렬 실행
        quick_sort(arr, pivot+1, right)

def lomuto_partition(arr, left, right):
    # 맨 오른쪽 요소를 pivot으로 설정하고,
    # i = left - 1
    # j = left
    pivot = arr[right]
    i = left - 1

    for j in range(left, right):
        # arr[j]가 pivot보다 작으면,
        if arr[j] < pivot:
            # i를 1 증가
            # arr[j]. arr[i] 위치 교환
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # i가 가리키는 위치가 pivot보다 작은 값의 마지막 인덱스
    # i + 1의 위치에 pivot를 두고 i+1 반환
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return j


T = int(input())
for tc in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    quick_sort(numbers, 0, N)
    print(numbers)
    print(numbers[N//2])