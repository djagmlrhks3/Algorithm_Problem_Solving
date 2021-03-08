def solution(stones, k):
    right = max(stones)+1
    left = 1
    while left < right-1:
        flag = True # k명이 건널 수 있는지 확인
        mid = (left + right) // 2
        cnt = 0
        for stone in stones:
            if stone < mid: # 건널 수 없는 경우 cnt + 1
                cnt += 1
            else:
                cnt = 0
            if cnt >= k: # cnt값이 k보다 같거나 크면 False
                flag = False
                break
        if flag: left = mid
        else: right = mid
    return left

solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)