import sys
sys.stdin=open('4530. 극한의 청소 작업.txt','r')
under100 = [4, 14, 24, 34, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 54, 64, 74, 84, 94]
T = int(input())
for tc in range(T):
    A, B = map(int,input().split())
    numA, numB = 0, 0
    flagA, flagB = True, True
    for i in under100:
        if flagA or flagB:
            if flagA and abs(A)%100 <= i:
                numA += under100.index(i)+1
                flagA = False
            if flagB and abs(B)%100 <= i:
                numB += under100.index(i)+1
                flagB = False
        else:
            break
    if abs(A) > 100:
        numA += (abs(A)//100)*len(under100)
    if abs(B) > 100:
        numB += (abs(B)//100)*len(under100)
    print(B-A-(numB+numA))