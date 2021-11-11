import sys
sys.stdin = open('백준4375. 1.txt', 'r')

while True:
    try:
        n = int(input())
        number = '1'
        while True:
            if not int(number) % n:
                print(len(number))
                break
            number += '1'
    except:
        break