import sys
input = sys.stdin.readline

A, B, C, M = map(int, input().split())

t = 0
fatigue = 0
task = 0

while True:
    if t>=24:
        break
    if fatigue + A > M:
        while True:
            if fatigue + A <= M or t>=24: break
            else :
                t+=1
                fatigue-=C
                if fatigue<=0:
                    fatigue=0
    else:
        t+=1
        fatigue+=A
        task+=B

print(task)

            
