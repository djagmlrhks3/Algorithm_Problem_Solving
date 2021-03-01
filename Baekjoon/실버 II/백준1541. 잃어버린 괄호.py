import sys
sys.stdin = open('백준1541. 잃어버린 괄호.txt', 'r')
# given = input().split('-')
# s = 0
# for i in given[0].split('+'):
#     s += int(i)
# for i in given[1:]:
#     for j in i.split('+'):
#         s -= int(j)
# print(s)

origin = input()
pm = '+-'
given, num = '', ''
for i in origin:
    if i not in pm:
        num += i
    else:
        given += str(int(num))
        given += i
        num = ''
given += str(int(num))
given.split('+')
while given.count('+'):
    plus = given.index('+')
    left, right = '', ''
    for idx in range(plus-1, -1, -1):
        if given[idx].isnumeric():
            left += given[idx]
        else:
            break
    for idx in range(plus+1, len(given)):
        if given[idx].isnumeric():
            right += given[idx]
        else:
            break
    given = given[:plus-len(left)] + str(int(left[::-1])+int(right)) + given[plus+len(right)+1:]
print(eval(given))
