def solution(n, k):
    def check(num):
        for i in range(2, int(num**(0.5)+1)):
            if not num % i:
                return False
        return True
    
    def convert(n, base):
        T = '0123456789ABCDEF'
        q, l = divmod(n, base)
        return convert(q, base) + T[l] if q else T[l]
    
    result = convert(n, k).split('0')
    answer, numbers = 0, []
    
    for num in result:
        if num.isdigit() and int(num) > 1:
            if check(int(num)):
                answer += 1
    return answer