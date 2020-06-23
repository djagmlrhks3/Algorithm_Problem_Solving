import sys
sys.stdin = open("4865. 글자수.txt","r")

T = int(input())
for tc in range(T):
    str1 = input()
    str2 = input()
    count = 0
    sample = list()

    for i in range(0,len(str1)):
        count = str2.count(str1[i])
        sample.append(count)

    print('#{} {}'.format(tc+1,max(sample)))