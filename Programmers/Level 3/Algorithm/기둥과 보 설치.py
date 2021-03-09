def check(answer):
    for c, r, a in answer:
        if a:
            if ([c-1, r, 1] in answer and [c+1, r, 1] in answer) or [c, r-1, 0] in answer or [c+1, r-1, 0] in answer:
                continue
            else:
                return False
        else:
            if not r or [c, r-1, 0] in answer or [c-1, r, 1] in answer or [c, r, 1] in answer:
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    answer = []
    for c, r, a, b in build_frame:
        if b:
            answer.append([c, r, a])
            if not check(answer):
                answer.remove([c, r, a])
        else:
            answer.remove([c, r, a])
            if not check(answer):
                answer.append([c, r, a])
    return sorted(answer)

solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])
# [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
