def solution(word):
    answer = 0
    vowels = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    weight = [781, 156, 31, 6, 1]
    for idx in range(len(word)):
        answer += vowels[word[idx]] * weight[idx]
    answer += len(word)
    return answer