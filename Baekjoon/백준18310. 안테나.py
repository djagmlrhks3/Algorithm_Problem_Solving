import sys
sys.stdin = open('백준18310. 안테나.txt', 'r')

N = int(input())
house = list(map(int, sys.stdin.readline().split()))
house.sort()
print(house[(len(house)-1)//2])
