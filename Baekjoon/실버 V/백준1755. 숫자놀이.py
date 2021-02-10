import sys
sys.stdin = open('백준1755. 숫자놀이.txt', 'r')

dictionary = {'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
M, N = map(int, input().split())

numbers = [[str(i)] for i in range(M, N+1)]
for num in numbers:
    word = ''
    for n in num[0]:
        word += dictionary[n]
    num.append(word)
cnt = 0
for num in sorted(numbers, key=lambda x:[x[1]]):
    print(int(num[0]), end=" ")
    cnt += 1
    if cnt == 10:
        print()
        cnt = 0

