import sys
sys.stdin = open('1289. 원재의 메모리 복구하기.txt','r')

T = int(input())
for tc in range(T):
    data = input()
    input_data = list()
    for i in data:
        input_data.append(i)
    count = 0
    while input_data.count('0') != len(input_data):
        for i in range(len(input_data)):
            if input_data[i] == '1':
                for j in range(i,len(input_data)):
                    if input_data[j] == '1':
                        input_data[j] = '0'
                    else:
                        input_data[j] = '1'
                count += 1
    print('#{} {}'.format(tc+1,count))