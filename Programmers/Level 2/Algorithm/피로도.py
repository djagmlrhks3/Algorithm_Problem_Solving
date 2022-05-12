from itertools import permutations

def solution(k, dungeons):
    answer = -1
    length = len(dungeons)
    for li in permutations(range(0, length), length):
        total = k
        cnt = 0
        for idx in li:
            if total >= dungeons[idx][0]:
                total -= dungeons[idx][1]
                cnt += 1
            else:
                break
        answer = max(answer, cnt)
    return answer