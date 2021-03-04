from collections import deque
def solution(n, t, m, timetable):
    queue = []
    bus = {}
    start = 9 * 60

    for i in range(n):
        bus[start+(i*t)] = []
    for time in timetable:
        time = time.split(":")
        queue.append(int(time[0]) * 60 + int(time[1]))

    queue.sort()
    queue = deque(queue)

    while queue:
        man = queue.popleft()
        for key in bus.keys():
            if man <= key and len(bus[key]) < m:
                bus[key].append(man)
                break

    for key in list(bus.keys())[::-1]:
        if len(bus[key]) < m:
            h, m = key // 60, key % 60
            break
        else:
            temp = bus[key][-1] - 1
            h, m = temp // 60, temp % 60
            break
    else:
        temp = bus[key][0] - 1
        h, m = temp // 60, temp % 60

    h = '0' + str(h) if h < 10 else str(h)
    m = '0' + str(m) if m < 10 else str(m)

solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"])