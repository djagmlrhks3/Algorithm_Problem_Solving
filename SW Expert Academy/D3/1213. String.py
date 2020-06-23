# import sys
# sys.stdin = open('1213. String.txt','r')

for tc in range(10):
    trash = input()
    find = input()
    data = input()
    print('#{} {}'.format(tc+1,data.count(find)))