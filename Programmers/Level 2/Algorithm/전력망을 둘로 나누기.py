def solution(n, wires):
    answer = n
    connect = {i:[] for i in range(1, n+1)}
    for v1, v2 in wires:
        connect[v1].append(v2)
        connect[v2].append(v1)

    for idx in range(len(wires)):
        v1, v2 = wires[idx]
        group = []
        visited = [0] * (n+1)
        for node in range(1, n+1):
            if len(group) > 2: break
            if not visited[node]:
                visited[node] = 1
                cnt = 1
                stack = [node]
                while stack:
                    start = stack.pop()
                    for end in connect[start]:
                        if min(start, end) == v1 and max(start, end) == v2: continue
                        if not visited[end]:
                            stack.append(end)
                            visited[end] = 1
                            cnt += 1
                group.append(cnt)
        else:
            answer = min(abs(group[0] - group[1]), answer)
    return answer