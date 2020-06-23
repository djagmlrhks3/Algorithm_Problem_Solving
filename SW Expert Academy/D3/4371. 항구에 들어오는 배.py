import sys
sys.stdin = open('4371. 항구에 들어오는 배.txt','r')

T = int(input())
for tc in range(T):
    N = int(input())
    hanggu = []
    for _ in range(N):
        hanggu.append(int(input()))
    # print(hanggu)

    jugi = []
    for i in range(1, N):
        jugi.append(hanggu[i] - hanggu[0])
    # print(jugi)

    for j in jugi:
        for k in jugi[jugi.index(j) + 1:]:
            if k % j == 0:
                jugi.remove(k)
    print(f'#{tc + 1} {len(jugi)}')
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     honeycombo = list()
#     for n in range(N):
#         before = int(input())
#         honeycombo.append(before-1)
#     count = 1
#     stack = list()
#     flag = False
#     while sum(honeycombo) != 0:
#         pick = honeycombo.pop(0)
#         if pick:
#             for i in range(len(honeycombo)):
#                 if honeycombo[i]%pick:
#                     flag = True
#                     continue
#                 else:
#                     honeycombo[i] = 0
#             if flag:
#                 count +=1
#                 flag = False
#     print('#{} {}'.format(tc+1,count))
# T=int(input())
#
# for tc in range(T):
#     N=int(input())
#     ship=[]
#     cnt=[[1] for _ in range(N)]
#     ans=0
#
#     for _ in range(N):
#         ship.append(int(input()))
#     for s in range(1,N):
#         a = 0
#         if s==1:
#             cnt[0].append(ship[s])
#         else:
#             while len(cnt[a])>1:
#                 a+=1
#             for j in range(a):
#                 if ship[s]-cnt[j][-1]==cnt[j][1]-cnt[j][0]:
#                     cnt[j].append(ship[s])
#                     cnt.pop(-1)
#                     break
#             else:
#                 cnt[a].append(ship[s])
#     while len(cnt[ans]) != 1:
#         ans += 1
#
#     print("#{} {}".format(tc+1,ans))
