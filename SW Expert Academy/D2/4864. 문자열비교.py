import sys
sys.stdin = open("4864. 문자열비교.txt","r")

T = int(input())
for tc in range(T):
    word1 = input()
    word2 = input()

    flag = True

    for i in range(0,len(word2)-len(word1)+1):
        test = ''
        for j in range(i,i+len(word1)):
            test += word2[j]
        if test == word1:
            print('#{} {}'.format(tc+1, 1))
            flag = True
            break
        else:
            flag = False

    if flag == False:
        print('#{} {}'.format(tc+1, 0))