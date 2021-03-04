def solution(lines):
    start, end = [], []
    traffics = len(lines)
    for line in lines:
        line = line.split(" ")
        h, m, s = list(map(float, line[1].split(':')))
        time = h * 3600 + m * 60 + s

        t = float(line[2][:-1])

        end.append(time + 1)
        start.append(time - t + 0.001)
    start.sort()
    answer, temp = 0, 0
    cs, ce = 0, 0
    while (ce < traffics) and (cs < traffics):
        if start[cs] < end[ce]:
            temp += 1
            answer = max(answer, temp)
            cs += 1
        else:
            temp -= 1
            ce += 1
    return answer

solution(
["2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"]
)