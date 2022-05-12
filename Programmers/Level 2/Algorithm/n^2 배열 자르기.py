def solution(n, left, right):
    answer = []
    for num in range(int(left), int(right+1)):
        share, rest = (num // n)+1, (num % n)
        if share > rest:
            answer.append(share)
        else:
            answer.append(rest+1)
    return answer