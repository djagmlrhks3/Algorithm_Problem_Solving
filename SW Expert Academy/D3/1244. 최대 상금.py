import sys
sys.stdin = open('1244. 최대 상금.txt', 'r')

#위치를 바꿔주는 함수
def swap(i, j):
    numbers[i], numbers[j] = numbers[j], numbers[i]


def solution(numbers, c):
    #0번부터 시작했으므로 count숫자와 c가 같으면 return
    if c == count:return

    #위치를 앞뒤로 바꿀거니까 range를 아래와 같이 정의 like 버블정렬
    #0번부터 len(numbers)-1 까지
    for i in range(len(numbers)-1):
        # i부터 len(numbers)까지
        for j in range(i+1, len(numbers)):
            swap(i, j) #i위치와 j위치 교환
            example = int(''.join(numbers)) #리스트에 담긴 숫자나열을 숫자로 변환
            if example not in candidate[c]: #만약 example이 candidate[c]에 이미 담겨있다면 넘어가자.
                candidate[c].append(example) #example이 candidate[c]에 담겨있지 않으면 append
                solution(numbers, c+1) # 교환횟수 c+1로 재귀
            swap(i, j)

T = int(input())
for tc in range(T):
    number, count = input().split()
    count = int(count)
    numbers = list(number)
    # result = ''.join(numbers) // 리스트 → 스트링

    # count만큼 교환한 숫자를 담는 리스트 for 메모이제이션(가지치기)
    candidate = [list() for _ in range(count)]

    solution(numbers, 0)
    print('#{} {}'.format(tc+1, max(candidate[count-1])))


