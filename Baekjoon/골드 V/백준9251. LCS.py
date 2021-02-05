import sys
sys.stdin = open('백준9251. LCS.txt', 'r')

string1 = input()
string2 = input()

DP = [[0] * (len(string1)+1) for _ in range(len(string2) + 1)]

for s2 in range(len(string2)):
    for s1 in range(len(string1)):
        if string2[s2] == string1[s1]:
            DP[s2+1][s1+1] = DP[s2][s1] + 1
        else:
            DP[s2+1][s1+1] = max(DP[s2][s1+1], DP[s2+1][s1])

print(DP[-1][-1])


