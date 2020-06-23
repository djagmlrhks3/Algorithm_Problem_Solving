import sys
sys.stdin=open('4366. 정식이의 은행업무.txt','r')

# def change(a,x):
#     s=''
#     while a>0:
#         a,r = divmod(a,x)
#         if r>9:
#             r=chr(ord('a')+r-10)
#         s=str(r)+s
#     print(s)

T=int(input())
for tc in range(T):
    two = input()[::-1]
    three = input()[::-1]
    sample_three = list()
    origin_two = 0
    origin_three = 0
    for i in range(len(two)):
        if int(two[i]):
            origin_two += 2**i
    for i in range(len(three)):
        if int(three[i]):
            origin_three += int(three[i]) * 3**i
    for j in range(len(three)):
        if int(three[j]) == 1:
            sample_three.append(origin_three+3**j)
            sample_three.append(origin_three-3**j)
        elif int(three[j]) == 2:
            sample_three.append(origin_three-3**j)
            sample_three.append(origin_three-2*3**j)
        else:
            sample_three.append(origin_three+3**j)
            sample_three.append(origin_three+2*3**j)
    for i in range(len(two)):
        if int(two[i]) and sample_three.count(origin_two-2**i) == 1:
            result = origin_two-2**i
            break
        elif int(two[i]) == 0 and sample_three.count(origin_two+2**i) == 1:
            result = origin_two+2**i
            break
    print('#{} {}'.format(tc+1,result))