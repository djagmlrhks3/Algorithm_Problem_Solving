"""
문자열에서 찾고자하는 문자의 인덱스 값 얻기
1. find  : 왼쪽 → 오른쪽
2. rfind : 오른쪽 → 왼쪽
"""
def solution(numbers):
    answer = []
    for num in numbers:
        binary = bin(num)[2:]
        cnt = binary.count('0')
        if cnt:
            index = binary.rfind('0')
            result = binary[:index] + '1' + binary[index+1:]
            if num%2:
                result = result[:index+1] + '0' + result[index+2:]
            answer.append(int('0b'+result, 2))
        else:
            result = '10' + '1' * (len(binary)-1)
            answer.append(int('0b'+result, 2))
    return answer