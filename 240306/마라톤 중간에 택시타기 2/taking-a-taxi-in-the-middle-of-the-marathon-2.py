import sys
def get_distance(isSkip):
    distance = 0
    for d in range(N-1):
        if isSkip[d]:
            continue
        nextidx = 1
        if isSkip[d+1]:
            nextidx += 1
        distance += abs(checkpoint[d][0]-checkpoint[d+nextidx][0])+abs(checkpoint[d][1]-checkpoint[d+nextidx][1])
    return distance


N = int(input())
checkpoint = [list(map(int,input().split())) for _ in range(N)]
answer = sys.maxsize
for skip in range(1,N-1):
    isSkip = [False for _ in range(N)]
    isSkip[skip] = True
    distance = get_distance(isSkip)
    if distance < answer:
        answer = distance
print(answer)