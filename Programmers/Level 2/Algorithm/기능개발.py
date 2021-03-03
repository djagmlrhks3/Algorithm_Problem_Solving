import math
def solution(progresses, speeds):
    answer = []
    idx = 0
    while idx < len(progresses):
        if progresses[idx] < 100:
            days = math.ceil((100 - progresses[idx]) / speeds[idx])
            for i in range(idx, len(progresses)):
                progresses[i] += (speeds[i] * days)
        else:
            for i in range(idx, len(progresses)):
                if progresses[i] < 100:
                    answer.append(i-idx)
                    idx = i
                    break
            else:
                answer.append(len(progresses)-idx)
                idx = len(progresses)
    return answer