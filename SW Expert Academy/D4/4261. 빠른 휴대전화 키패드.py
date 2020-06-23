import sys
sys.stdin=open('4261. 빠른 휴대전화 키패드.txt','r')
keypad = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
T = int(input())
for tc in range(T):
    S, N = input().split()
    words = input().split()
    count = 0
    for i in words:
        if len(i) != len(S):
            words.remove(i)
    for i in words:
        flag = True
        for j in range(len(S)):
            if i[int(j)] not in keypad[int(S[j])]:
                flag = False
                break
        if flag:
            count +=1
    print('#{} {}'.format(tc+1,count))
