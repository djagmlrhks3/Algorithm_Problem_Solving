from itertools import permutations
def solution(n, weak, dist):
    weak += [n+w for w in weak]
    answer = len(dist) + 1
    for start in range(len(weak)//2):
        for friend in permutations(dist, len(dist)):
            cnt = 1
            position = weak[start] + friend[cnt - 1]
            for idx in range(start, start + len(weak)//2):
                if position < weak[idx]:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    position = weak[idx] + friend[cnt - 1]
            answer = min(answer, cnt)
    if answer > len(dist):
        return - 1
    return answer

solution(12, [1, 5, 6, 10], [1, 2, 3, 4])